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
      await this.loginUser(this.user).catch((e) => {
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
      } else {
        this.error = true
        setTimeout(() => {
          this.error = false
        }, 3000)
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
  <div class="d-flex justify-content-center align-items-center flex-column">
    <form
      class="container form d-flex flex-column justify-content-center align-items-center"
      @submit.prevent="login"
    >
      <h1 class="text-center h3 pb-5 own_golden_title">Iniciar sesión</h1>
      <img
        src="/logo_club.svg"
        class="mb-3 w-100"
        alt="club deportivo villa elisa"
        style="max-width: 200px"
      />
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
      <button type="submit" class="btn own_btn w-100">Iniciar sesión</button>
    </form>
    <div
      v-if="error"
      class="alert alert-danger mt-3 d-flex justify-content-center align-items-center text-center"
      role="alert"
    >
      Credenciales incorrectas
    </div>
  </div>
</template>

<style scoped>
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
form {
  max-width: 800px;
  width: 100%;
}
</style>
