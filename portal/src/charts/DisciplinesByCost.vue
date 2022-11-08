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
import { getAssociates } from "../services/AssociateDataService"


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
      scales: {
        y: {
          stacked: true,
          ticks: {
            beginAtZero: true,
            callback: function (value:Number) {
              if (value % 1 === 0) {
                return value
              }
            },
          },
        },
      },
      title: {
          display: true,
          text: "Cantidad de inscriptos a disciplinas particulares",
          font: { size: 24 },
        },
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
      const disciplines = res.data
      const disciplinesAmount = disciplines.map((discipline) => {
        return {
          [discipline.name +
          " " +
          discipline.category +
          " " +
          discipline.dates]: 0,
        }
      })

      const associates = await getAssociates()
      const associatesDisciplines = associates.data.map((associate) => {
          return associate.disciplines!.map((discipline) => discipline.name +
          " " +
          discipline.category +
          " " +
          discipline.dates)
      }).flat()
      disciplinesAmount.forEach((discipline) => {
        const disciplineName = Object.keys(discipline)[0]
        discipline[disciplineName] = associatesDisciplines.filter((discipline) => discipline === disciplineName).length
      })

      disciplinesAmount.sort(
        (a, b) => Object.values(b)[0] - Object.values(a)[0]
      )
      function dynamicColors() {
        var r = Math.ceil(Math.random() * 255)
        var g = Math.ceil(Math.random() * 255)
        var b = Math.ceil(Math.random() * 255)
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
        labels: disciplinesAmount.map((discipline) =>
          Object.keys(discipline)
        ),
        datasets: [
          {
            label: "Cantidad de inscriptos",
            backgroundColor: poolColors(disciplinesAmount.length),
            data: disciplinesAmount.map(
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
