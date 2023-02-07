<script setup>
    import { useStore } from "../stores";
    
    const store = useStore();
    const { updateSkin } = store;
</script>

<template>
    <div id="dashboard">
        <h2>Calendar Overview</h2>
        <h3>Current Quests</h3>
        <p class="delius">You have an assignment due tomorrow for COMP2080!</p>
        <h2>Choose a UI Skin</h2>
        <div class="skins">
            <div :class="`skin-preview skin-default`" @click="updateSkin('skin-default')" />
            <div :class="`skin-preview skin-forest`" @click="updateSkin('skin-forest')" />
            <div :class="`skin-preview skin-sunset`" @click="updateSkin('skin-sunset')" />
        </div>
        <slot />
    </div>
</template>

<style scoped>
    #dashboard{
        margin-bottom: 10vh;
    }

    .skins{
        display: flex;
        margin: 1em 0 1em 0;
    }

    .skin-preview{
        height: 4em;
        width: 6em;
        margin: 0 0.5em 0 0.5em;
        border: 2px solid var(--gold);
        border-radius: 0.5em;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        cursor: pointer;
    }

    .skin-preview:hover{
        transition: 0.3s;
        filter: brightness(110%) opacity(80%);
    }
</style>