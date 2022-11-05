<template>
  <div class="text-center">
    <h1>Estadisticas</h1>
    <div class="card own_main_holder">
      <div class="card-body text-center statistics_body">
        <BarChart />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import BarChart from "../charts/DisciplinesByGender.vue"
import { defineComponent } from "vue"

export default defineComponent({
  name: "Statistics",
  components: { BarChart },
})
</script>

<style>
@media only screen and (max-width: 767px),
  (min-width: 768px) and (max-width: 1024px) {
  .chart {
    width: 100%;
  }
}

.own_main_holder {
  width: 100%;
  padding: 20px;
  align-items: center;
  border: 0px;
}
.statistics_body {
  margin-top: 20px;
  width: 80%;
  padding: 20px;
}
</style>
