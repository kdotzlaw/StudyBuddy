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
        reqs: {type: Array, required: false, default: []},
    })

    // Start or pause study for selected class
    function manageStudy(className){
        setStudyClass(className);
        Mgmt.manageTimer(userId.value,className);
    }
</script>

<template>
    <div id="classCards">
        
        <!-- Class card set -->
        <div v-for="req in reqs" :class="`classCard studyClass`">
            <router-link :to="'/class/' + req.class_Name">
                
                <!-- Class name -->
                <h3> {{ req.class_Name }} </h3>

            </router-link>
            <div class="bottom-row">

                <!-- Time studied -->
                <div>
                    <span class="material-symbols-outlined">timer</span>
                    &nbsp; {{ (req.studyTime/3600).toFixed(2) }} hrs 
                </div>

                <!-- Play control -->
                <img
                    v-if="req.class_Name != studyClass" 
                    class="play-btn" 
                    :src="Play" 
                    alt="Study for this class"
                    @click="manageStudy(req.class_Name)"
                />

            </div>
        </div>

        <!-- Add New card -->
        <router-link to="/createClass">
            <div :class="`classCard addNew`"> + </div>
        </router-link>
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
        min-height: 100px;
        width: 190px;
        border-radius: 20px;
        cursor: pointer;
        margin: 2vh 0.5vw 2vh 0.5vw;
        box-shadow: inset 0.1em 0.1em 0.3em rgba(0,0,0,0.4);
    }

    .addNew{
        border: 3px solid var(--border-disabled);
        color: var(--border-disabled);
        display: grid;
        justify-items: center;
        align-items: center;
        font-size: 50px;
        line-height: 30px;
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