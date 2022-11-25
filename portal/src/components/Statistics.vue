<template>
  <div class="text-center">
    <h1 class="own_golden_title">Estadisticas</h1>
    <div class="card own_main_holder">
      <div class="card-body text-center statistics_body">
        <DisciplinesByGender />
      </div>
      <div class="card-body text-center statistics_body">
        <UpToDateAssociates />
      </div>
      <div class="card-body text-center statistics_body">
        <DisciplinesByAssociates />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import DisciplinesByGender from '../charts/DisciplinesByGender.vue'
import DisciplinesByAssociates from '../charts/DisciplinesByAssociates.vue'
import UpToDateAssociates from '../charts/UpToDateAssociates.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Statistics',
  components: {
    DisciplinesByGender,
    UpToDateAssociates,
    DisciplinesByAssociates,
  },
})
</script>

<style>
@media only screen and (max-width: 767px),
  (min-width: 768px) and (max-width: 1024px) {
  .chart {
    width: 100%;
  }
}
@media only screen and (max-width: 767px) {
  .statistics_body {
    width: 100% !important;
    padding: 0px !important;
  }
  .own_main_holder {
    padding: 0px !important;
  }
}

.own_main_holder {
  width: 100%;
  padding: 20px;
  align-items: center;
  border: 0px;
}
.statistics_body {
  width: 80%;
  margin-bottom: 5rem;
}
</style>
