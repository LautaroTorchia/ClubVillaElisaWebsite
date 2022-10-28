<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Navbar from './components/Navbar.vue'
</script>

<template>
  <Navbar/>
  <div class="container p-5">
    <router-view></router-view>
  </div>
  
</template>

<style scoped></style>
