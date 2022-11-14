<script lang="ts">
import { defineComponent } from 'vue'
import { Payment } from '../interfaces/Payment'
import { getPayments, createPayment } from '../services/PaymentService'
export default defineComponent({
  data() {
    return {
      payments: [] as Payment[] | string,
    }
  },
  methods: {
    async loadPayments() {
      const id = '1' // WARNING: get from jwt
      const res = await getPayments(id)
      this.payments = res.data
    },
    async createPayment() {
      const id = '1' // WARNING: get from jwt
      const res = await createPayment(id)
      console.log(res)
    },
  },
  mounted() {
    this.loadPayments()
  },
})
</script>

<template>
  <div>
    <h1>Payments</h1>
    <div v-for="(payment, index) in payments" :key="index">
      <p>id: {{ payment.id }} | monto: {{ payment.amount }}</p>
      <p>date: {{ payment.date }} | numero de cuota: {{ payment.installment_number }}</p>
    </div>
    <h1>Realizar Pago</h1>
    <button @click="this.createPayment()">Pagar</button>
  </div>
</template>

<style scoped></style>
