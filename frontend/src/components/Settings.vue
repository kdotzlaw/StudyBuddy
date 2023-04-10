<!-- 
  Settings.vue 
    Manage application appearance and settings.
-->

<script setup>
    import { onMounted } from "vue";
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    import Corgi from "./Corgi.vue";
    import Bunny from "./Bunny.vue";
    import Parakeet from "./Parakeet.vue";
    
    const store = useStore();
    const { uiSkin } = storeToRefs(store);
    const { updateSkin, updateBuddy } = store;

    // Add a box glow on current UI skin
    onMounted(() => {
        let selected = document.querySelector(`.skins .${uiSkin.value}`);
        selected.classList.add("skin-active");
    });

    // Swap UI skin and transfer box glow when applicable
    function updateTheSkin(skinId){
        updateSkin(skinId);

        let skins = document.getElementsByClassName("skin-preview");
        for(let skin of skins){
            skin.classList.remove("skin-active");
            if(skin.classList.contains(skinId))
                skin.classList.add("skin-active");
        }
    }

    // Swap buddy choice
    function updateTheBuddy(buddyId){
        updateBuddy(buddyId);
    }
</script>

<template>
    <div class="settings-container">
        <h2>Update UI Skin</h2>
        <div class="skins">
            <div :class="`skin-preview skin-default`" @click="updateTheSkin('skin-default')" />
            <div :class="`skin-preview skin-forest`" @click="updateTheSkin('skin-forest')" />
            <div :class="`skin-preview skin-sunset`" @click="updateTheSkin('skin-sunset')" />
        </div>
        <h2>Swap Buddy</h2>
        <div class="buddies">
            <div :class="`buddy-preview`" @click="updateTheBuddy('Corgi')">
                <Corgi />
            </div>
            <div :class="`buddy-preview`" @click="updateTheBuddy('Bunny')">
                <Bunny />
            </div>
            <div :class="`buddy-preview`" @click="updateTheBuddy('Parakeet')">
                <Parakeet />
            </div>
        </div>
    </div>
</template>

<style scoped>
    .settings-container{
        display: grid;
        justify-items: center;
    }
    
    .skins, .buddies{
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
        filter: brightness(130%) opacity(80%);
    }

    .skin-preview:active{
        filter: brightness(30%);
    }

    .skin-active{
        box-shadow: 0 0 6px 2px var(--highlight);
    }

    .buddy-preview{
        height: 7em;
        width: 6em;
        margin: 0 2em 0 2em;
        cursor: pointer;
    }

    .buddy-preview:hover{
        transition: 0.3s ease-in-out;
        transform: scale(110%);
    }

    .buddy-preview svg{
        height: inherit;
        transform: translateX(-30%);
    }
</style>