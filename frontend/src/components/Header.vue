<script setup>
    import { storeToRefs } from "pinia";
    import { ref } from "vue";
    import Logo from "/assets/logo.png";
    import Play from "/artifacts/play.svg";
    import Pause from "/artifacts/pausegold.png";
    import Timer from "../logic/timer";
    import Mgmt from "../logic/managetimer";
    import { useStore } from "../stores";
    const store = useStore();
    
    // Temporary env vars
    let displayName = "My Buddy";
    const { loginUser, logoutUser } = store;
    const { userId, studyClass, pageName } = storeToRefs(store);

    /*===========================
       TIMER MANAGEMENT
     *===========================*/

    // Current study time in milliseconds
    const { studyTime } = storeToRefs(store);

    // Parse seconds into hh:mm:ss time string
    function toTimeString(s){
        let timeString = ""
        let hours = Math.floor(s / 3600);
        if(hours > 0)
            timeString += hours.toString(10).padStart(2, "0") + ":"
        s = s % 3600;
        let minutes = Math.floor(s / 60);
        let seconds = s % 60;
        return ( 
            timeString + 
            minutes.toString(10).padStart(2, "0") + ":" + 
            seconds.toString(10).padStart(2, "0")
        );
    }

    // Pause button ref. Switch between pause and time view on hover
    const showPause = ref(false);

    function switchPause(newVal){
        showPause.value = newVal;
    }

    /*===========================
       DROPDOWN MENU AND MODALS
     *===========================*/
    const { setModal } = store;

    // Toggle dropdown options on click and mouse events
    const showOptions = ref(false);
    function switchOptions(newVal){
        showOptions.value = newVal;
    }

    // Execute option
    function settings(){
        setModal("Settings", "settings", "Made with ❤️ The Procrastinators © 2023");
    }

    function logOut(){
        logoutUser();
        setModal("Log out", "success", "You successfully logged out. See you soon!");
    }

    function login(){
        loginUser("user123");
        setModal("Login", "login");
    }

    function register(){
        setModal("Create Account", "register");
    }
</script>

<template>
    <div id="header">
        <h1 class="pageNameSection">
            {{ pageName }}
        </h1>
        <div v-if="studyClass" class="timerSection">
            <div>Currently studying for <b>{{ studyClass }}</b></div>
            <button 
                id="timerExpress"
                @click="Mgmt.manageTimer(userId,studyClass)"
                @mouseover="switchPause(true)"
                @mouseleave="switchPause(false)"
            >
                <div v-if="showPause">
                    <img :src=Pause alt="Pause study session" />
                </div>
                <div v-else>
                    {{ toTimeString(studyTime) }}
                </div>
            </button>
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
            <button class="dropdown-tab" @click="settings">
                Manage Settings
            </button>
            <button class="dropdown-tab" @click="logOut">
                Log Out
            </button>
            <button class="dropdown-tab" @click="login">
                Login
            </button>
            <button class="dropdown-tab" @click="register">
                Register
            </button>
        </div>
    </div>
</template>

<style scoped>
    #header{
        position: absolute;
        height: 13vh;
        width: 100vw;
        z-index: 10;
        color: var(--fadegold);
        background: var(--darkteal);
        display: grid;
        grid-template-columns: 25% 1fr 20%;
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

    .timerSection{
        justify-self: center;
        display: grid;
        grid-template-columns: max-content 5em;
        justify-items: center;
        align-items: center;
    }

    #timerExpress{
        margin-left: 1vw;
        border-radius: 0.8em;
        border: 3px solid var(--gold);
        background: var(--button);
        color: var(--fadegold);
        height: 2.5em;
        width: max-content;
        min-width: 3.5em;
        padding: 0;
        overflow: hidden;
        display: grid;
        justify-items: center;
        align-items: center;
    }

    #timerExpress div{
        font-size: 1.2em;
        min-width: 3em;
        box-shadow: inset 2px 2px 4px rgba(0,0,0,0.3);
        padding: 0 0.5em 0 0.5em;
    }

    #timerExpress:active{
        filter: brightness(0.3);
        transition: 0.5;
    }

    #timerExpress img{
        height: 1em;
        width: max-content;
        margin-top: 0.4em;
    }

    .userSection{
        height: 12vh;
        margin-top: 0.5vh;
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
        font-family: 'Gabriela', serif;
    }

    #header-dropdown .dropdown-tab{
        font-size: 15px;
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