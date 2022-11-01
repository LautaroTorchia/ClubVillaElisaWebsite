
<template>
    <div>
        <b-table hover :disciplines="disciplines">
            
        </b-table>
    </div>
</template>


<script lang="ts">
    import { defineComponent } from 'vue'
    import { Discipline } from '../interfaces/Discipline'
    import { getDisciplines } from '../services/DisciplinesService'
    export default defineComponent({
        data() {
            return {
                disciplines: [] as Discipline[] | string,
            }
        },
        methods: {
            async getDisciplines() {
                const res = await getDisciplines()
                this.disciplines = res.data
            }
        },
        mounted() {
            this.getDisciplines()
        }
    });
</script>


<style>
    
</style>