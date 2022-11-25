<template>
  <h4>Cantidad de inscriptos a disciplinas particulares</h4>
  <div class="container">
    <Bar v-if="loaded" :chart-data="chartData" :chart-options="chartOptions" />
  </div>
</template>

<script lang="ts">
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  SubTitle,
} from 'chart.js'

import { getDisciplines } from '../services/DisciplinesService'
import { getAssociates } from '../services/AssociateDataService'
import { defineComponent } from 'vue'

ChartJS.register(
  Title,
  SubTitle,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
)

export default defineComponent({
  name: 'DisciplinesByAssociatesBarChart',
  components: { Bar },
  data() {
    return {
      loaded: false,
      chartData: { datasets: [] as any, labels: [] as any },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            ticks: {
              callback: function (value: number) {
                if (value % 1 === 0) {
                  return value
                }
              },
            },
          },
        },
      },
    }
  },
  async mounted() {
    this.loaded = false
    try {
      const res = await getDisciplines()
      const disciplines = res.data
      const disciplinesAmount = disciplines.map((discipline) => {
        return {
          [discipline.name]: 0,
        }
      })

      const associates = await getAssociates()
      const associatesDisciplines = associates.data
        .map((associate) => {
          return associate.disciplines!.map((discipline) => discipline.name)
        })
        .flat()
      disciplinesAmount.forEach((discipline) => {
        const disciplineName = Object.keys(discipline)[0]
        discipline[disciplineName] = associatesDisciplines.filter(
          (discipline) => discipline === disciplineName
        ).length
      })

      disciplinesAmount.sort(
        (a, b) => Object.values(b)[0] - Object.values(a)[0]
      )
      function dynamicColors() {
        var r = Math.ceil(Math.random() * 255)
        var g = Math.ceil(Math.random() * 255)
        var b = Math.ceil(Math.random() * 255)
        return 'rgba(' + r + ',' + g + ',' + b + ', 0.8)'
      }
      function poolColors(a: any) {
        var pool = []
        for (let i = 0; i < a; i++) {
          pool.push(dynamicColors())
        }
        return pool
      }

      this.chartData = {
        labels: disciplinesAmount.map((discipline) => Object.keys(discipline)),
        datasets: [
          {
            label: 'Cantidad de inscriptos',
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
})
</script>
