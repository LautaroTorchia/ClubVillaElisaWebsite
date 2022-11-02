
<template>
    <div>
        <p> {{ disciplines }} </p>
        <table id="tableComponent" class="table table-bordered table-striped">
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