<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="own_main_body">
    <Navbar />
    <main class="container p-5">
      <router-view></router-view>
    </main>
  </div>
  <Footer />
</template>

<style scoped>

</style>
