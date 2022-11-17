<template>
  <div class="container">
    <Doughnut
      v-if="loaded"
      :chart-data="chartData"
      :chart-options="chartOptions"
    />
  </div>
</template>

<script lang="ts">
import { Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  ChartDataset,
} from 'chart.js'

import { getUpToDateAssociates } from '../services/UpToDateAmountService'
import { defineComponent } from 'vue'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default defineComponent({
  name: 'DoughnutChart',
  components: { Doughnut },
  data() {
    return {
      loaded: false,
      chartData: { datasets: [] as any, labels: [] as any },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            display: true,
            text: 'Proporcion de usuarios deudores',
            font: { size: 24 },
          },
        },
      },
    }
  },
  async mounted() {
    this.loaded = false
    try {
      const res = await getUpToDateAssociates()

      this.chartData = {
        labels: ['Adeuda', 'No Adeuda'],
        datasets: [
          {
            backgroundColor: ['#E46651', '#41B883'],
            data: Object.values(res.data),
          },
        ],
      }

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
})
</script>
