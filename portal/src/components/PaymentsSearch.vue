<template>
  <div>
    <input type="text" />
    <button class="bt-secondary"></button>
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
          <th>DNI</th>
          <th>Fecha de nacimiento</th>
          <th>Disciplina</th>
          <th>Fecha de pago</th>
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
      search: "",
      searchBy: "name",
      searchByOptions: [
        { value: "name", text: "Nombre" },
        { value: "email", text: "Email" },
        { value: "dni", text: "DNI" },
        { value: "phone", text: "Teléfono" },
      ],
    };
  },
  components: {
  },
  methods: {
    async searchPayments() {
      const response = await fetch(
        `http://localhost:3000/payments?${this.searchBy}=${this.search}`
      );
      this.payments = await response.json();
      console.log(this.payments);
    },
  },
  mounted() {
    this.searchPayments();
  },
});
</script>

<style></style>
