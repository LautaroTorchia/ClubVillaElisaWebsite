<script lang="ts">
import { defineComponent } from 'vue'
import { Payment } from '../interfaces/Payment'
import { getPayments, createPayment } from '../services/PaymentService'
import { getConfiguration } from '../services/ConfigurationService'
import { Configuration } from '../interfaces/Configuration'

export default defineComponent({
  data() {
    return {
      user: {
        name: '',
        surname: '',
        entry_date: new Date(),
        actual_amount: 0,
        payments: [] as Payment[],
      },
      associate_number: 1,
      config: {} as Configuration,
      paymentToPay: {} as Payment | undefined,
      showModal: false,
      image: '' as string,
      count: 0,
    }
  },
  methods: {
    async loadPayments() {
      const res = await getPayments(this.associate_number)
      this.user = res.data
      if (res.data.payments) this.user.payments = res.data.payments.reverse()
      if (this.user.entry_date)
        this.user.entry_date = new Date(this.user.entry_date)
      this.createUnpaidPayments()
      this.paymentToPay = this.user.payments.find(
        (p) => p.installment_number == -1
      )
    },
    async createPayment() {
      this.closeModal()
      const res = await createPayment(this.associate_number, this.image).catch(
        (err) => {
          this.loadPayments()
        }
      )
      this.loadPayments()
    },

    createUnpaidPayments() {
      const today = new Date()
      if (
        (this.user.payments && this.user.payments.length != 0) ||
        (this.user.entry_date &&
          this.user.entry_date.getMonth() <= today.getMonth() &&
          this.user.entry_date.getFullYear() <= today.getFullYear())
      ) {
        // get max date from payments
        this.user.entry_date.setMonth(this.user.entry_date.getMonth() - 1)
        const lastPaymentDate =
          this.user.payments.length > 0
            ? new Date(this.user.payments[0].date)
            : this.user.entry_date
        const diff = today.getTime() - lastPaymentDate.getTime()
        const diffDays = Math.ceil(diff / (1000 * 3600 * 24))
        let installment_number = -1
        const unpaidPayments = Math.floor(diffDays / 30)
        for (let i = 0; i < unpaidPayments; i++) {
          const newPayment = {
            id: '0',
            installment_number: installment_number,
            date: new Date(
              new Date(lastPaymentDate.getTime()).setMonth(
                lastPaymentDate.getMonth() + i + 1
              )
            ),
            amount: this.user.actual_amount,
            paid_late: false,
          }
          this.user.payments.unshift(newPayment)
          installment_number--
        }
      }
    },
    async getConfig() {
      const res = await getConfiguration()
      this.config = res.data
    },
    changeImage(e: any) {
      const image = e.target.files[0]
      const reader = new FileReader()
      reader.readAsDataURL(image)
      reader.onload = (e: any) => {
        this.image = e.target.result
      }
    },
    closeModal() {
      this.showModal = false
      this.image = ''
      this.count++
    },
  },
  mounted() {
    this.getConfig()
  },
})
</script>

<template>
  <h1 class="own_golden_title">Pagos</h1>
  <div class="d-flex justify-content-center input-group" id="searchPayment">
    <div class="input-group-prepend">
      <label for="associate_number" class="rounded-0 m-0 input-group-text"
        >Número de socio:
      </label>
    </div>
    <input
      type="number"
      id="searchId"
      v-model="associate_number"
      class="form-control"
      style="min-width: 85px; max-width: 300px"
    />
    <div class="input-group-append">
      <button
        class="btn btn-light rounded-0 border"
        @click="loadPayments"
        action
      >
        Buscar
      </button>
    </div>
  </div>
  <div name="asociado">
    <p></p>
  </div>
  <div>
    <div v-if="user.name == null">
      <h3 class="text-center">No se encontró un asociado con ese número</h3>
    </div>
    <div v-if="user.payments && user.payments.length == 0 && user.name">
      <h3 class="text-center">
        No se encontraron pagos para {{ user.name }} {{ user.surname }}
      </h3>
    </div>
    <table
      v-if="user.payments && user.payments.length > 0"
      id="tableComponent"
      class="table table-bordered table-striped"
    >
      <thead>
        <tr class="text-center">
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Fecha de cuota</th>
          <th>Monto</th>
          <th>Estado</th>
          <th>Acción</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(data, index) in user.payments"
          :key="index"
          class="text-center"
        >
          <td style="--title1: 'Nombre'">{{ user.name }}</td>
          <td style="--title2: 'Apellido'">{{ user.surname }}</td>
          <td style="--title3: 'Fecha de cuota'">
            {{
              new Date(data.date).toLocaleDateString('es-ES', {
                month: 'long',
                year: 'numeric',
              })
            }}
          </td>
          <td style="--title4: 'Monto'">
            {{ data.amount }} {{ config.currency }}
          </td>
          <td style="--title5: 'Estado'">
            {{
              data.installment_number < 0
                ? 'No esta paga'
                : data.paid_late
                ? 'Pago tarde'
                : 'Pago a tiempo'
            }}
          </td>
          <td style="--title6: 'Acción'">
            <button
              v-if="data.installment_number == -1"
              class="btn btn-outline-secondary"
              @click="showModal = true"
            >
              Pagar
            </button>
            <p v-if="data.installment_number != -1"></p>
          </td>
        </tr>
      </tbody>
    </table>
    <div>
      <!-- First modal -->
      <vue-final-modal
        v-model="showModal"
        classes="modal-container"
        content-class="modal-content"
      >
        <a
          class="modal__close mx-2"
          @click="closeModal"
          style="cursor: pointer"
        >
          <font-awesome-icon icon="fa-solid fa-times" />
        </a>
        <span class="modal__title">Subir Comprobante</span>
        <div
          class="modal__content d-flex justify-content-center flex-column align-items-center"
        >
          <label for="image" class="my-3"
            >Archivo de comprobante a subir
          </label>
          <input
            class="form-control"
            type="file"
            name="image"
            id="image"
            style="min-height: 38px; width: 90%"
            @change="changeImage"
            :key="count"
          />
          <img
            v-if="image"
            :src="image"
            alt="Foto del comprobante"
            class="img-fluid mt-4"
            style="max-height: 500px; height: 100%"
          />
        </div>
        <div class="modal__action">
          <button
            class="btn btn-outline-secondary mx-2"
            v-if="image"
            @click="createPayment()"
          >
            Confirmar
          </button>
          <button class="btn btn-outline-danger mx-2" @click="closeModal">
            Cancelar
          </button>
        </div>
      </vue-final-modal>
    </div>
  </div>
</template>

<style scoped>
::v-deep .modal-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
::v-deep .modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  max-height: 90%;
  margin: 0 1rem;
  padding: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.25rem;
  background: #fff;
  max-width: 1024px;
  z-index: 100001 !important;
}
.modal__title {
  margin: 0 2rem 0.5rem 0;
  font-size: 1.5rem;
  font-weight: 700;
}
.modal__content {
  flex-grow: 1;
  overflow-y: auto;
}
.modal__action {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  padding: 1rem 0 0;
}
.modal__close {
  position: absolute;
  color: black;
  top: 0.5rem;
  right: 0.5rem;
}
</style>
