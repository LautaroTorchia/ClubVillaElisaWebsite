<script lang="ts">
  import { defineComponent } from 'vue'
  import { Discipline } from '../interfaces/Discipline'
  import { Card } from '../interfaces/Card'
  import { getMyDisciplines } from '../services/DisciplinesService'
  import { getMyCard } from "../services/AssociateDataService";
  import { mapGetters } from 'vuex'
  export default defineComponent({
    data() {
      return {
        disciplines: [] as Discipline[] | string,
        associate_card: [] as Card[] | string,
      }
    },
    computed: {
      ...mapGetters({
        authUser: 'auth/user',
      }),
    },
    methods: {
      async loadMyDisciplines() {
        const res = await getMyDisciplines()
        this.disciplines = res.data
        console.log(res.data)
      },
      async loadMyCard() {
        const res = await getMyCard()
        this.associate_card= res.data
        console.log(res.data)
      },
    },
    mounted() {
      this.loadMyDisciplines()
      this.loadMyCard()
    }
})
</script>
<template>
  <div>
    <h1>Datos de {{ authUser.name }} {{ authUser.surname }}</h1>
    <h2>Disciplinas:</h2>
    <div v-for="(discipline, index) in disciplines" :key="index">
      <p>Disciplina: {{ discipline.name }} | Categoria: {{ discipline.category }}</p>
      <p>Precio: {{ discipline.price }} | Instructores: {{ discipline.teacher }}</p>
      <p>Horario: {{ discipline.days }} </p>
    </div>
  </div>
  <div>
    <h2>Mi Carnet</h2>
    <img :src="'data:image/jpg;base64,' + associate_card.associate_card " alt="Associate Carnet" />
  </div>
</template>

<style scoped></style>
