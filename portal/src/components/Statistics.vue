<template>
  <div style = "width: 500px;">
    <BarChart />
  </div>
</template>

<script lang="ts">
import BarChart from '../charts/chart'

export default {
  name: 'App',
  components: { BarChart }
}
</script>

<style>
@media screen and (min-width: 300px) {
  .chart {
    width: 100%;
  }
}

</style>
