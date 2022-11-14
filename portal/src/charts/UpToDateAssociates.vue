<template>
  <div class="container">
    <Doughnut v-if="loaded" :chart-data="chartData" :chart-options="chartOptions" />
  </div>
</template>

<script lang="ts">
import { Doughnut } from "vue-chartjs"
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from 'chart.js'

import { getUpToDateAssociates } from "../services/UpToDateAmountService"

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default {
  name: "DoughnutChart",
  components: { Doughnut },
  data: () => ({
    loaded: false,
    chartData: {},
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: "Proporcion de usuarios deudores",
          font: { size: 24 },
        },
      },
    },
  }),
  async mounted() {
    this.loaded = false
    try {
      const res = await getUpToDateAssociates()

      this.chartData = {
        labels: ["Adeuda", "No Adeuda"],
        datasets: [
          {
            backgroundColor: [ "#E46651","#41B883"],
            data: Object.values(res.data),
          },
        ],
      }

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
}
</script>
