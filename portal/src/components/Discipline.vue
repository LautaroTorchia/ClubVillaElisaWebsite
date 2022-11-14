<script lang="ts">
import { defineComponent } from 'vue'
import { mapGetters } from 'vuex'
export default defineComponent({
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
    }),
  },
})
</script>

<template>
  <div>
    <h1>Disciplinas</h1>
    <p>Usuario: {{ authUser.username }}</p>
  </div>
</template>

<style scoped></style>
