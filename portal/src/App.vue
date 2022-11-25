<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div>
    <Navbar />
    <main class="container own_main_body">
      <router-view></router-view>
    </main>
  </div>
  <Footer />
</template>

<style scoped>
@media (width < 768px) and (width >= 360px) {
  .own_main_body {
    padding: 20px !important;
  }
}

@media (width < 360px) {
  .own_main_body {
    padding: 0 !important;
  }
}
</style>
