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
@media only screen and (max-width: 767px),
  (min-width: 768px) and (max-width: 1024px)  {
  .chart {
    width: 100%;
  }
}

</style>
