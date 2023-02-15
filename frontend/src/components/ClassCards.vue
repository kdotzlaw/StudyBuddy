<script setup>
    import { ref } from "vue";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { setStudyClass } = store;

    const props = defineProps({ 
        reqs: {type: Array, required: false, default: []}
    })

    const reqs = ref(props.reqs);

</script>

<template>
    <div id="classCards">
        <div v-if="reqs.length==0" :class="`classCard addNew`"> + </div>
        <div v-for="req in reqs" :class="`classCard studyClass`" @click="setStudyClass(req.name)">
            <router-link to="/class">
                <h3> {{ req.name }} </h3>
            </router-link>
            <div>
                <span class="material-symbols-outlined">timer</span>
                &nbsp; {{ req.timeStudied }} hrs 
            </div>
        </div>
    </div>
</template>

<style scoped>
    #classCards{
        margin-top: 2em;
        height: 90%;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;
    }

    .classCard{
        height: max-content;
        min-height: 3.2em;
        width: 9.5em;
        border-radius: 0.8em;
        cursor: pointer;
        margin: 1em 0.5em 1em 0.5em;
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

    .studyClass{
        border: 3px double var(--border);
        display: flex;
        flex-direction: column;
        padding: 0 0 0.8em 0.8em;
        line-height: 15px;
    }

    .studyClass:nth-child(1){
        background: var(--red);
    }
    .studyClass:nth-child(2){
        background: var(--blue);
    }
    .studyClass:nth-child(3){
        background: var(--green);
    }
    .studyClass:nth-child(4){
        background: var(--yellow);
    }

    .studyClass h3{
        color: var(--white);
        font-weight: 200;
        font-size: 30px;
    }

    .studyClass div{
        color: var(--text-disabled);
        display: flex;
        align-items: center;
    }
    .studyClass:hover{
        transition: 0.5s ease-out;
        filter: brightness(120%);
        opacity: 0.9;
        border-color: var(--richgold);
    }
    .studyClass:active{
        background: var(--black);
    }

    
</style>