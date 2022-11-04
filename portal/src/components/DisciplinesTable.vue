<script lang="ts">
    import { defineComponent } from 'vue'
    import { DisciplineClub } from '../interfaces/Discipline'
    import { getDisciplines } from '../services/DisciplinesService'
    import { BTable } from 'bootstrap-vue'
    export default defineComponent({
        data() {
            return {
                disciplines: [] as DisciplineClub[]
            }
        },
        components: {
            BTable
        },
        methods: {
            async getDisciplines() {
                const res = await getDisciplines()
                this.disciplines = res.data
                console.log(res.data)
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
                    <th> Instructores </th>
                    <th> Días y horarios </th>
                </tr>
            </thead>
            <tbody>
                <!-- Loop through the list get the each student data -->
                <tr v-for="(data, index) in disciplines" :key='index' class="text-center">
                    <td> {{data.name}} </td>
                    <td> {{data.teacher}} </td>
                    <td> {{data.dates}} </td>
                </tr>
            </tbody>
        </table> 
    </div>
</template>




<style>
    
</style>