<script lang="ts">
import { defineComponent } from 'vue'
import { Discipline } from '../interfaces/Discipline'
import { Card } from '../interfaces/Card'
import { getMyDisciplines } from '../services/DisciplinesService'
import { getMyCard } from '../services/AssociateDataService'
import { getConfiguration } from '../services/ConfigurationService'
import { Configuration } from '../interfaces/Configuration'
import { mapGetters } from 'vuex'
export default defineComponent({
  data() {
    return {
      disciplines: [] as Discipline[],
      associate_card: {} as Card,
      config: {} as Configuration,
    }
  },
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
    }),
  },
  methods: {
    async loadMyDisciplines() {
      await getMyDisciplines().then((res) => {
        this.disciplines = res.data
      })
    },
    async loadMyCard() {
      await getMyCard().then((res) => {
        this.associate_card = res.data
      })
    },
    async getConfig() {
      const res = await getConfiguration()
      this.config = res.data
    },
  },
  mounted() {
    this.loadMyDisciplines()
    this.loadMyCard()
    this.getConfig()
  },
})
</script>
<template>
  <div>
    <h1 class="own_golden_title">
      Datos de {{ authUser.name }} {{ authUser.surname }}
    </h1>
    <h2>Disciplinas anotadas:</h2>
    <div>
      <table
        id="tableComponent"
        class="table table-bordered table-striped"
        v-if="disciplines.length > 0"
      >
        <thead>
          <tr class="text-center">
            <!-- loop through each value of the fields to get the table header -->
            <th>Disciplina</th>
            <th>Categoría</th>
            <th>Instructores</th>
            <th>Días y horarios</th>
            <th>Costo mensual</th>
          </tr>
        </thead>
        <tbody>
          <!-- Loop through the list get the each student data -->
          <tr
            v-for="(discipline, index) in disciplines"
            :key="index"
            class="text-center"
          >
            <td style="--title1: 'Disciplina'">{{ discipline.name }}</td>
            <td style="--title2: 'Categoría'">{{ discipline.category }}</td>
            <td style="--title3: 'Instructores'">{{ discipline.teacher }}</td>
            <td style="--title4: 'Días y horarios'">{{ discipline.days }}</td>
            <td style="--title5: 'Costo mensual'">
              ${{ discipline.price }} {{ config.currency }}
            </td>
          </tr>
        </tbody>
      </table>
      <div v-else>
        <h3 class="text-center">
          No se encontraron Disciplinas para {{ authUser.name }}
          {{ authUser.surname }}
        </h3>
      </div>
    </div>
  </div>
  <div class="d-flex flex-column align-center">
    <h2>Carnet de socio:</h2>
    <img
      :src="'data:image/jpg;base64, ' + associate_card.associate_card"
      alt="Associate Carnet"
      class="img-fluid align-self-center w-100 mb-4"
      style="max-width: 650px"
    />
  </div>
</template>

<style scoped></style>
