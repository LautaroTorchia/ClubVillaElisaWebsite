<template>
  <div class="container">
    <Bar v-if="loaded" :chart-data="chartData" :chart-options="chartOptions" />
  </div>
</template>

<script lang="ts">
import { Bar } from "vue-chartjs"
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js"
import { Associate } from "../interfaces/Associate"
import { getAssociates } from "../services/AssociateDataService"

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: "BarChart",
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: {},
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true,
        },
      },
    },
  }),
  async mounted() {
    this.loaded = false
    try {
      const res = await getAssociates()

      const associates_by_gender = Array.from(
        res.data
          .reduce(
            (m, v: Associate) =>
              m.set(v.gender, [...(m.get(v.gender) || []), v]),
            new Map()
          )
          .values()
      )
      //Array de arrays de asociados por genero

      const disciplines = res.data.map((associate) => associate.disciplines)

      this.chartData = {
        labels: Array.from(
          { length: Number(res.years[1]) - Number(res.years[0]) + 1 },
          (_, i) => String(Number(res.years[0]) + i)
        ),
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#ff00ff",
            data: [1, 2, 3],
          },
          {
            label: "Data 2",
            backgroundColor: "#f00fff",
            data: [1, 2, 3],
          },
          {
            label: "Data 3",
            backgroundColor: "#f8ff79",
            data: [1, 2, 3],
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
