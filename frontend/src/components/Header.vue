<script setup>
    // Javascript
    // Props
    // Imports
</script>

<template>
    <div id="header">
        <div id="pageNameSection">
            Page Name
        </div>
        <div id="timerSection">
            Current time 0:00
        </div>
        <div id="userSection">
            Welcome User123!
        </div>
    </div>
</template>

<style scoped>
    #header{
        color: wheat;
        display: grid;
        grid-template-columns: 25% 1fr 20%;
        text-align: center;
    }

    #pageNameSection{
        background: darkcyan;
    }
    
    #timerSection{
        background: darkslategray;
    }
    
    #userSection{
        background: darkgreen;
    }
</style>