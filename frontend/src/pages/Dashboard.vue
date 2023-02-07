<script setup>
    let userId = "User123";
</script>

<template>
    <div id="dashboard">
        <h2>Calendar Overview</h2>
        <h3>Current Quests</h3>
        <p class="delius">You have an assignment due tomorrow for COMP2080!</p>
        <slot />
    </div>
</template>

<style scoped>
    #dashboard{
        margin-bottom: 10vh;
    }
</style>