<script lang="ts">
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'
export default defineComponent({
  data() {
    return {
      error: false,
      user: {
        username: '',
        password: '',
      },
    }
  },
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
      isLoggedIn: 'auth/isLoggedIn',
    }),
  },
  methods: {
    ...mapActions('auth', ['loginUser', 'logoutUser']),
    async login() {
      await this.loginUser(this.user).catch(() => {
        // Handle error
        this.error = true
      })
      //Cleaning
      this.user = {
        username: '',
        password: '',
      }

      if (this.isLoggedIn) {
        this.$router.push('/')
      }
    },
    async logout() {
      await this.logoutUser().catch((err) => {
        console.log(err)
      })
      this.error = false
      this.user = {
        username: '',
        password: '',
      }
      this.$router.push('/')
    },
  },
})
</script>

<template>
  <div class="col-md-4 offset-md-4">
    <form class="form d-flex flex-column justify-content-center align-items-center" @submit.prevent="login">
      <h1 class="text-center h3 pb-5 own_golden_title">Iniciar sesión</h1>
      <img src="/logo_club.svg" class="mb-3 w-100" alt="club deportivo villa elisa" style="max-width:200px">
      <input
        type="text"
        v-model="user.username"
        placeholder="Nombre de usuario"
        class="form-control mb-3"
      />
      <input
        type="password"
        v-model="user.password"
        placeholder="Contraseña"
        class="form-control mb-3"
      />
      <button type="submit" class="btn btn-secondary btn-block w-100">
        Iniciar sesión
      </button>
    </form>
  </div>
</template>

<style scoped></style>
