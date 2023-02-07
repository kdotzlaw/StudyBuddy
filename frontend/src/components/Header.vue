<script setup>
    import { ref } from "vue";
    import Logo from "/assets/logo.png";
    import { useStore } from "../stores";

    const store = useStore();
    const { setModal } = store;

    let displayName = "User123";

    // Toggle dropdown options on click and mouse events
    const showOptions = ref(false);
    function switchOptions(newVal){
        showOptions.value = newVal;
    }

    // Execute option
    function openSettings(){
        setModal("Settings");
    }

    function logOut(){
        setModal("Log out", "<button>Imagine this will Log you Out</button>");
    }
</script>

<template>
    <div id="header">
        <h1 id="pageNameSection">
            Page Name
        </h1>
        <div id="timerSection">
            Current time 0:00
        </div>
    </div>
    <div 
        id="header-dropdown"
        class="dropdown-tab"
        @click="switchOptions(!showOptions)"
        @mouseover="switchOptions(true)"
        @mouseleave="switchOptions(false)"
    >
        <div class="userSection">
            <img class="logo-thumb" :src='Logo' alt="Study Buddy logo" />
            <div> Welcome <b>{{displayName}}</b>! </div>
        </div>
        
        <div v-if="showOptions">
            <button class="dropdown-tab" @click="openSettings">
                Manage Settings
            </button>
            <button class="dropdown-tab" @click="logOut">
                Log Out
            </button>
        </div>
    </div>
</template>

<style scoped>
    #header{
        position: absolute;
        width: 100vw;
        z-index: 10;
        color: var(--fadegold);
        background: var(--darkteal);
        display: grid;
        grid-template-columns: 20% 1fr 20%;
        grid-gap: 5%;
        text-align: center;
        align-items: center;
        box-shadow: 0 0.5em 1em rgba(0,0,0,0.3);
    }

    #header-dropdown{
        position: absolute;
        z-index: 11;
        right: 0;
        height: max-content;
        width: 20%;
        display: flex;
        flex-direction: column;
    }

    .userSection{
        height: 12vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .dropdown-tab{
        background: var(--teal);
        color: var(--text);
        border: 2px solid var(--darkerteal);
        height: 12vh;
        width: 100%;
        cursor: pointer;
    }

    .dropdown-tab:not(:nth-child(1)){
        border-top-style: none;
    }

    .dropdown-tab:hover{
        background-color: var(--lightteal);
        opacity: 0.9;
        transition: 0.2s ease-out;
    }

    .logo-thumb{
        height: 2em;
        width: 2em;
        margin: 0 0.5em 0.5em 0;
    }
</style>