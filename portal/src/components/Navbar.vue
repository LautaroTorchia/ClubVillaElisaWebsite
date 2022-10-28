<script lang="ts">
export default {
  setup() {},
}
</script>

<template>
  <nav class="navbar navbar-expand-md sticky-top navbar-shrink py-3 bg-white">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/"
        ><img
          src="/logo_club.svg"
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
      <div
        class="collapse navbar-collapse d-flex justify-content-between"
        id="navbarNav"
      >
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/disciplinas"
              >Disciplinas</router-link
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
          <li class="nav-item">
            <router-link class="nav-link" to="/autenticar"
              >Iniciar sesion</router-link
            >
          </li>
        </ul>
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
}
.bg-white{
  background-color: white;
}
</style>
