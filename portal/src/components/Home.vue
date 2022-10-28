<script lang="ts">
  import { ref } from 'vue'
  import Carousel from './DisciplinesCarousel.vue'

  export default {
    name: 'Home',
    components: { 
      Carousel
    }, 
    setup() {
      const count = ref(0)
      return {
        count,
      }
    },
  }
</script>


<template>
  <Carousel></Carousel>
  <h1>Aca estaria el carousel con disciplinas</h1>
  <button @click="count++">Increment</button>
  <p>Count is: {{ count }}</p>
</template>


<style scoped></style>
