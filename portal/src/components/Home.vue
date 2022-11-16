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
  import PaymentsSearch from './PaymentsSearch.vue'
  import { defineComponent } from 'vue'

  export default defineComponent({
    name: 'Home',
    components: { 
      Carousel,
      DiscTable,
      PaymentsSearch
    }, 
  })
</script>


<style scoped>
.own_golden_title {
  padding-top: 1rem;
  padding-bottom: 1rem;
  text-shadow: 0px -5px 5px rgba(181, 161, 102, 0.5);
  font-family: Amaranth, sans-serif;
  text-align: center;
  width: auto;
}
.holder{
  background-color: #fafafa;
  box-shadow: 0 -2px 20px #00000015;
}
</style>
