<script lang="ts">
    import { defineComponent } from 'vue'
    import { DisciplineClubWithCosts } from '../interfaces/Discipline'
    import { getDisciplinesWithCosts } from "../services/DisciplinesService"
    import { BTable } from 'bootstrap-vue'
    export default defineComponent({
        data() {
            return {
                disciplines: [] as DisciplineClubWithCosts[]
            }
        },
        components: {
            BTable
        },
        methods: {
            async getDisciplines() {
                const res = await getDisciplinesWithCosts()
                this.disciplines = res.data
            }
        },
        mounted() {
            this.getDisciplines()
        }
    });
</script>


<template>
    <div>
        <table id="tableComponent" class="table table-bordered table-striped">
            <thead>
                <tr class="text-center">
                    <!-- loop through each value of the fields to get the table header -->
                    <th> Nombre </th>
                    <th> Categoría </th>
                    <th> Instructores </th>
                    <th> Días y horarios </th>
                    <th> Costo mensual </th>
                </tr>
            </thead>
            <tbody>
                <!-- Loop through the list get the each student data -->
                <tr v-for="(data, index) in disciplines" :key='index' class="text-center">
                    <td> {{data.name}} </td>
                    <td> {{data.category}} </td>
                    <td> {{data.teacher}} </td>
                    <td> {{data.dates}} </td>
                    <td> ${{data.monthly_cost}} </td>
                </tr>
            </tbody>
        </table> 
    </div>
</template>




<style>
    
</style>