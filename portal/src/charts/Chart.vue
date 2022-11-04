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
          barThickness: 0.1,
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
      let dict = {}
      res.data.map((assoc) =>
          assoc.disciplines.map((discip) => {
            let d = new Date(discip.associated_at).getFullYear()
            if (dict[assoc.gender] == undefined){
              dict[assoc.gender]={}
            }
            if (dict[assoc.gender][d] == undefined) {
              dict[assoc.gender][d] = 1
            } else {
              dict[assoc.gender][d] += 1
            }
          })
        )
      const disciplines = res.data.map((associate) => associate.disciplines)

      this.chartData = {
        labels: 
        Array.from(
          { length: Number(res.years[1]) - Number(res.years[0]) + ((Number(res.years[1]) - Number(res.years[0])) <10 ?10:1)},
          (_, i) => String(Number(res.years[0]) + i)
        ),
        datasets: [
          {
            label: "Hombres",
            backgroundColor: "#ffad08",
            data: Object.values(dict.male),
          },
          {
            label: "Mujeres",
            backgroundColor: "#73b06f",
            data: Object.values(dict.female),
          },
          {
            label: "Otro",
            backgroundColor: "#405059",
            data: Object.values(dict.other),
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
