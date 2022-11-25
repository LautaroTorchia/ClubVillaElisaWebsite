<template>
  <div>
    <div class="holder">
      <h1 class="own_golden_title">Club Deportivo Villa Elisa</h1>
      <Carousel></Carousel>
    </div>
    <h2 class="own_golden_title mt-5">Disciplinas</h2>
    <DiscTable class="mt-2"></DiscTable>
  </div>
</template>

<script lang="ts">
import Carousel from './DisciplinesCarousel.vue'
import DiscTable from './DisciplinesTable.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Home',
  components: {
    Carousel,
    DiscTable,
  },
})
</script>

<style scoped>
.holder {
  background-color: #fafafa;
  box-shadow: 0 -2px 20px #00000015;
}
</style>
