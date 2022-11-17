<script lang="ts">
import { defineComponent } from 'vue'
import { Discipline } from '../interfaces/Discipline'
import { Card } from '../interfaces/Card'

import { getMyDisciplines } from '../services/DisciplinesService'
import { getMyCard } from "../services/AssociateDataService";
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
      const id = '2' // WARNING: get from jwt
      const res = await getMyDisciplines(id)
      this.disciplines = res.data
    },
    async loadMyCard() {
      const id = '1' // WARNING: get from jwt
      const res = await getMyCard(id)
      this.associate_card = res.data
    },
  },
  mounted() {
    this.loadMyDisciplines()
    this.loadMyCard()

</script>

<template>
  <div>
    <h1>Mis Disciplinas</h1>
    <p>Usuario: {{ authUser.username }}</p>
    <div v-for="(discipline, index) in disciplines" :key="index">
      <p>Disciplina: {{ discipline.name }} | Categoria: {{ discipline.category }}</p>
      <p>Precio: {{ discipline.price }} | Instructores: {{ discipline.teacher }}</p>
      <p>Horario: {{ discipline.days }} </p>
    </div>
  </div>
  <div>
    <h1>Mi Carnet</h1>
     {{ associate_card.associate_card }}
    <h1>Disciplinas</h1>
    
  </div>
</template>

<style scoped></style>
