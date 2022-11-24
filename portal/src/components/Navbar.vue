<script lang="ts">
import { defineComponent } from 'vue'
import { mapActions, mapGetters } from 'vuex'

export default defineComponent({
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
      isLoggedIn: 'auth/isLoggedIn',
    }),
  },
  methods: {
    ...mapActions('auth', ['logoutUser']),
    async logout() {
      await this.logoutUser().catch((err) => {
        console.log(err)
      })
      this.$router.push('/autenticar')
    },
  },
})
</script>

<template>
  <nav class="navbar navbar-expand-md sticky-top navbar-shrink py-3 bg-light">
    <div class="container">
      <router-link class="navbar-brand" to="/"
        ><img
          src="/logo_club.svg"
          width="100px"
          class="logo"
          alt="club deportivo villa elisa"
      /></router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <router-link class="nav-link" to="/disciplinas"
              >Mis datos</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/pagos">Pagos</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/estadisticas"
              >Estadísticas</router-link
            >
          </li>
        </ul>
        <router-link
          v-if="!isLoggedIn"
          class="btn own_btn px-3 d-flex justify-content-center"
          to="/autenticar"
          >Iniciar sesion</router-link
        >
        <router-link
          v-if="isLoggedIn"
          @click="logout"
          class="btn own_btn px-3 d-flex justify-content-center"
          to="/autenticar"
          >Cerrar sesion</router-link
        >
      </div>
    </div>
  </nav>
</template>

<style scoped>
.logo {
  width: 80px;
}
nav {
  border-bottom: 1px solid rgba(45, 45, 45, 0.1);
  z-index: 10 !important;
  background-color: rgb(250, 250, 250) !important;
}
.nav-link {
  text-align: center;
}
.own_btn {
  background: #b5a166;
  color: #333;
  border: solid 1px transparent;
  border-radius: 5px;
  font-weight: 700;
  transition: 0.3s;
}
.own_btn:hover {
  border: solid 1px #333 !important;
  background: transparent !important;
}
.btn.active {
  background: #b5a166;
  border: solid 1px transparent;
}
</style>
