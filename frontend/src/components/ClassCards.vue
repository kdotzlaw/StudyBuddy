<!-- 
  ClassCards.vue 
    Renders a set of cards from a user's classes. Cards contain the class name, time studied, and Play control.
-->

<script setup>
    import { ref } from "vue";
    import { storeToRefs } from "pinia";
    import Play from "/artifacts/play.svg";
    import Mgmt from "../logic/managetimer";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { setStudyClass } = store;
    const { userId, studyClass } = storeToRefs(store);

    const props = defineProps({ 
        reqs: {type: Array, required: false, default: []}
    })

    // Start or pause study for selected class
    function manageStudy(className){
        setStudyClass(className);
        Mgmt.manageTimer(userId.value,className);
    }
</script>

<template>
    <div id="classCards">
        
        <!-- Add New card -->
        <div v-if="reqs.length==0" :class="`classCard addNew`"> + </div>
        
        <!-- Class card set -->
        <div v-for="req in reqs" :class="`classCard studyClass`">
            <router-link to="/class">
                
                <!-- Class name -->
                <h3> {{ req.name }} </h3>

            </router-link>
            <div class="bottom-row">

                <!-- Time studied -->
                <div>
                    <span class="material-symbols-outlined">timer</span>
                    &nbsp; {{ req.timeStudied }} hrs 
                </div>

                <!-- Play control -->
                <img
                    v-if="req.name != studyClass" 
                    class="play-btn" 
                    :src="Play" 
                    alt="Study for this class"
                    @click="manageStudy(req.name)"
                />

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
        min-height: 6em;
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
        border-color: var(--richgold);
    }
    .studyClass:active{
        background: var(--black);
    }

    .bottom-row{
        display: flex;
        justify-content: space-between;
        margin-right: 1em;
    }

    .play-btn{
        height: 1.2em;
        width: 1.5em;
        cursor: pointer;
    }

    .play-btn:hover{
        transition: 0.5s ease-out;
        filter: brightness(120%);
    }

    
</style>