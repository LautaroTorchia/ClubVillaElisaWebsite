<template>
  <footer
    class="text-center text-lg-start bg-light position-relative bottom-0 top-0 w-100"
  >
    <div
      class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom"
    >
      <div class="me-5 d-none d-lg-block">
        <span>Podes comunicarte con nosotros mediante:</span>
      </div>
      <div
        class="d-flex justify-content-between align-items-center"
        style="min-width: 100px"
      >
        <a
          target="_blank"
          href="https://www.facebook.com/eldepove"
          class="text-reset"
        >
          <font-awesome-icon icon="fa-brands fa-facebook me-3" />
        </a>
        <a
          target="_blank"
          href="https://twitter.com/deportivove"
          class="text-reset"
        >
          <font-awesome-icon icon="fa-brands fa-twitter me-3" />
        </a>
        <a
          target="_blank"
          href="https://www.instagram.com/eldepove/"
          class="text-reset"
        >
          <font-awesome-icon icon="fa-brands fa-instagram me-3" />
        </a>
      </div>
    </div>
    <section class="">
      <div class="container text-center text-md-start mt-5">
        <div class="row mt-3">
          <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">
              Club Deportivo Villa Elisa
            </h6>
            <p>Primer club histórico de la ciudad</p>
          </div>
          <div
            class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4 d-flex justify-content-center"
          >
            <img
              alt="Logo del Club"
              src="/logo_club.svg"
              style="height: 10rem"
            />
          </div>

          <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">Contacto</h6>
            <p>
              <font-awesome-icon icon="fa-solid fa-home me-3" /> Camino
              Centenario y 48
            </p>
            <p>Villa Elisa, La Plata</p>
            <p>
              <font-awesome-icon icon="fa-solid fa-phone me-3" /> {{ info }}
            </p>
          </div>
        </div>
      </div>
    </section>
  </footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getInfo } from '../services/InfoService'
export default defineComponent({
  data() {
    return {
      info: '',
    }
  },
  methods: {
    async getInfo() {
      const res = await getInfo()
      this.info = res.data.Contacto
    },
  },
  mounted() {
    this.getInfo()
  },
})
</script>

<style scoped>
footer {
  background-color: rgb(250, 250, 250) !important;
  color: rgb(78, 93, 120);
}
</style>
