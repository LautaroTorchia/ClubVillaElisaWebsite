<script lang="ts">
import { defineComponent } from 'vue'
import { DisciplineClubWithCosts } from '../interfaces/Discipline'
import { getDisciplinesWithCosts } from '../services/DisciplinesService'
import { getConfiguration } from '../services/ConfigurationService'
import { Configuration } from '../interfaces/Configuration'
import { BTable } from 'bootstrap-vue'
export default defineComponent({
  data() {
    return {
      disciplines: [] as DisciplineClubWithCosts[],
      config: {} as Configuration,
    }
  },
  components: {
    BTable,
  },
  methods: {
    async getDisciplines() {
      const res = await getDisciplinesWithCosts()
      this.disciplines = res.data
    },
    async getConfig() {
      const res = await getConfiguration()
      this.config = res.data
    },
  },
  mounted() {
    this.getDisciplines(), this.getConfig()
  },
})
</script>

<template>
  <div>
    <table id="tableComponent" class="table table-bordered table-striped">
      <thead>
        <tr class="text-center">
          <!-- loop through each value of the fields to get the table header -->
          <th>Nombre</th>
          <th>Categoría</th>
          <th>Instructores</th>
          <th>Días y horarios</th>
          <th>Costo mensual</th>
        </tr>
      </thead>
      <tbody>
        <!-- Loop through the list get the each student data -->
        <tr
          v-for="(data, index) in disciplines"
          :key="index"
          class="text-center"
        >
          <td style="--title1: 'Nombre'">{{ data.name }}</td>
          <td style="--title2: 'Categoría'">{{ data.category }}</td>
          <td style="--title3: 'Instructores'">{{ data.teacher }}</td>
          <td style="--title4: 'Días y horarios'">{{ data.dates }}</td>
          <td style="--title5: 'Costo mensual'">
            ${{ data.monthly_cost }} {{ config.currency }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style></style>
