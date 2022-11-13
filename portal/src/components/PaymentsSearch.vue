<template>
  <div class="d-flex justify-content-center">
    <input type="number" id="searchId" class="own_input"/>
    <button class="btn btn-light" action>Buscar</button>
  </div>
  <div name="asociado">
    <p></p>
  </div>
  <div>
    <table id="tableComponent" class="table table-bordered table-striped">
      <thead>
        <tr class="text-center">
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Disciplina</th>
          <th>Fecha de cuota</th>
          <th>Monto</th>
          <th>Estado</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(data, index) in payments" :key="index" class="text-center">
          <td>{{ data }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>



<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "PaymentsSearch",
  data() {
    return {
      payments: [],
    };
  },
  components: {
  },
  methods: {
    async searchPayments() {
      const id = document.getElementById("searchId") as HTMLInputElement;
      const response = await fetch(
        `http://localhost:3000/payments${id}`
      );
      this.payments = await response.json();
      console.log("Pagos: ", this.payments)
    },
  },
  mounted() {
    this.searchPayments();
  },
});
</script>



<style>
  .own_input {
    min-width: 10%;
    max-width: 30%;
    margin-right: 1rem;
  }
</style>
