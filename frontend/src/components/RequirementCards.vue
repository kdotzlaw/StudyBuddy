<script setup>
    import { ref } from "vue";
    const props = defineProps({ 
        reqs: {type: Array, required: false, default: []}
    })

    const reqs = ref(props.reqs);
</script>

<template>
    <div id="reqCards">
        <div v-if="reqs.length==0" :class="`reqCard addNew`"> + </div>
        <div v-for="req in reqs" :class="`reqCard fullCard`">
            <h3> {{ req.name }} </h3>
            <div>
                <span class="material-symbols-outlined">timer</span>
                &nbsp; {{ req.timeStudied }} hrs 
            </div>
        </div>
    </div>
</template>

<style scoped>
    #reqCards{
        margin: 1em 0 2em 0;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;
    }

    .reqCard{
        height: 18vh;
        width: 100%;
        border-radius: 0.8em;
        cursor: pointer;
        margin: 0 0.5em 1em 0.5em;
        box-shadow: inset 0.1em 0.1em 0.3em rgba(0,0,0,0.4);
    }

    .addNew{
        border: 3px solid var(--border-disabled);
        color: var(--border-disabled);
        display: grid;
        justify-items: center;
        align-items: center;
        font-size: 30px;
        line-height: 30px;
        font-weight: 900;
    }

    .addNew:hover{
        transition: 0.5s ease-out;
        filter: brightness(120%);
    }

    .fullCard{
        border: 3px double var(--border);
        display: flex;
        flex-direction: column;
        padding: 0 0 0.8em 0.8em;
        line-height: 15px;
    }

    .fullCard h3{
        color: var(--white);
        font-weight: 200;
        font-size: 30px;
    }
    
</style>