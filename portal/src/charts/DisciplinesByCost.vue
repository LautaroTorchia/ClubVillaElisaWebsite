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
  SubTitle,
} from "chart.js"

import { getDisciplinesWithCosts } from "../services/DisciplinesService"
import Discipline from "../components/Discipline.vue"

ChartJS.register(
  Title,
  SubTitle,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
)

export default {
  name: "BarChartCost",
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: {},
    chartOptions: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: "Precio de las disciplinas",
          font: { size: 24 },
        },
      },
    },
  }),
  async mounted() {
    this.loaded = false
    try {
      const res = await getDisciplinesWithCosts()
      console.log(res.data)
      //take res.data and map it to a list of objects of the kind discipline.name+discipline.dates: discipline.cost
      const disciplines = res.data
      const disciplinesWithCosts = disciplines.map((discipline) => {
        return {
          [discipline.name +
          " " +
          discipline.category +
          " " +
          discipline.dates]: Number(discipline.monthly_cost),
        }
      })
      disciplinesWithCosts.sort(
        (a, b) => Object.values(b)[0] - Object.values(a)[0]
      )
      function dynamicColors() {
        var r = Math.floor(Math.random() * 255)
        var g = Math.floor(Math.random() * 255)
        var b = Math.floor(Math.random() * 255)
        return "rgba(" + r + "," + g + "," + b + ", 0.8)"
      }
      function poolColors(a) {
        var pool = []
        for (let i = 0; i < a; i++) {
          pool.push(dynamicColors())
        }
        return pool
      }

      this.chartData = {
        labels: disciplinesWithCosts.map((discipline) =>
          Object.keys(discipline)
        ),
        datasets: [
          {
            backgroundColor: poolColors(disciplinesWithCosts.length),
            data: disciplinesWithCosts.map(
              (discipline) => Object.values(discipline)[0]
            ),
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
