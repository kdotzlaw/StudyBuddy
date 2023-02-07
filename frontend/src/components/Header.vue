<script setup>
    import Logo from "/assets/logo.png";

    let displayName = "User123";
</script>

<template>
    <div id="header">
        <h1 id="pageNameSection">
            Page Name
        </h1>
        <div id="timerSection">
            Current time 0:00
        </div>
        <div id="userSection">
            <img class="logo-thumb" :src='Logo' alt="Study Buddy logo" />
            <div> Welcome <b>{{displayName}}</b>! </div>
        </div>
    </div>
</template>

<style scoped>
    #header{
        color: var(--fadegold);
        background: var(--darkteal);
        display: grid;
        grid-template-columns: 25% 1fr 20%;
        text-align: center;
        align-items: center;
        box-shadow: 0 0.5em 1em rgba(0,0,0,0.3);
    }
    
    #userSection{
        height: 100%;
        width: 100%;
        background: var(--teal);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .logo-thumb{
        height: 2em;
        width: 2em;
        margin: 0 0.5em 0.5em 0;
    }
</style>