
<template>
    <div>
        <p> {{ disciplines }} </p>
        <table id="tableComponent" class="table table-bordered table-striped">
            <thead>
                <tr>
                    <!-- loop through each value of the fields to get the table header -->
                    <th v-for="(k, v, index) in disciplines" :key='index'> 
                        {{k}} <i class="bi bi-sort-alpha-down" aria-label='Sort Icon'></i>
                    </th>
                </tr>
            </thead>
            <tbody>
                <!-- Loop through the list get the each student data -->
                <tr v-for="(k, v, index) in disciplines" :key='index'>
                    <td v-for="(k, v, index2) in disciplines" :key='index2'>
                        {{v}}
                    </td>
                </tr>
            </tbody>
        </table> 
    </div>
</template>


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


<style>
    
</style>