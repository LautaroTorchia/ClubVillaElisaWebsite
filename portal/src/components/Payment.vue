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
    },
    async createPayment() {
      const res = await createPayment(this.associate_number)
      this.loadPayments()
    },

    createUnpaidPayments() {
      const today = new Date()
      if (
        this.user.payments && this.user.payments.length != 0 ||
        (this.user.entry_date && this.user.entry_date.getMonth() < today.getMonth() &&
          this.user.entry_date.getFullYear() <= today.getFullYear())
      ) {
        // get max date from payments
        const lastPaymentDate =
          this.user.payments.length > 0
            ? new Date(this.user.payments[0].date)
            : this.user.entry_date
        const diff = today.getTime() - lastPaymentDate.getTime()
        const diffDays = Math.ceil(diff / (1000 * 3600 * 24))
        let installment_number = -1
        if (diffDays > 30) {
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
      }
    },
    async getMorosityFee() {
      const res = await getConfiguration()
      this.config = res.data
    },
  },
  mounted() {
    this.getMorosityFee()
  },
})
</script>

<template>
  <h1 class="own_golden_title mt-5">Pagos</h1>
  <div class="d-flex justify-content-center input-group">
    <div class="input-group-prepend">
      <label for="associate_number" class="rounded-0 m-0 input-group-text"
        >Número de asociado:
      </label>
    </div>
    <input
      type="number"
      id="searchId"
      v-model="associate_number"
      class="form-control"
      style="min-width: 100px"
    />
    <div class="input-group-append">
      <button class="btn btn-secondary rounded-0" @click="loadPayments" action>
        Buscar
      </button>
    </div>
  </div>
  <div name="asociado">
    <p></p>
  </div>
  <div>
    <div v-if="user.payments && user.payments.length == 0 && user.name">
      <h3 class="text-center">No se encontraron pagos para {{ user.name }}</h3>
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
          <th>Accion</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(data, index) in user.payments"
          :key="index"
          class="text-center"
        >
          <td>{{ user.name }}</td>
          <td>{{ user.surname }}</td>
          <td>{{ new Date(data.date).toLocaleDateString('es-ES') }}</td>
          <td>{{ data.amount }} {{ config.currency }}</td>
          <td>
            {{
              data.installment_number < 0
                ? 'No esta paga'
                : data.paid_late
                ? 'Pago tarde'
                : 'Pago a tiempo'
            }}
          </td>
          <td>
            <button
              v-if="data.installment_number == -1"
              class="btn btn-secondary"
              @click="createPayment"
            >
              Pagar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
