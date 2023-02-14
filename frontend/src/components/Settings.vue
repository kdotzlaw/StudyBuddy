<script setup>
    import { onMounted } from "vue";
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    
    const store = useStore();
    const { uiSkin } = storeToRefs(store);
    const { updateSkin } = store;

    onMounted(() => {
        let selected = document.querySelector(`.skins .${uiSkin.value}`);
        selected.classList.add("skin-active");
    });

    function updateTheSkin(skinId){
        updateSkin(skinId);

        let skins = document.getElementsByClassName("skin-preview");
        for(let skin of skins){
            skin.classList.remove("skin-active");
            if(skin.classList.contains(skinId))
                skin.classList.add("skin-active");
        }
    }
</script>

<template>
    <h2>Update UI Skin</h2>
    <div class="skins">
        <div :class="`skin-preview skin-default`" @click="updateTheSkin('skin-default')" />
        <div :class="`skin-preview skin-forest`" @click="updateTheSkin('skin-forest')" />
        <div :class="`skin-preview skin-sunset`" @click="updateTheSkin('skin-sunset')" />
    </div>
</template>

<style scoped>
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
        filter: brightness(130%) opacity(80%);
    }

    .skin-preview:active{
        filter: brightness(30%);
    }

    .skin-active{
        box-shadow: 0 0 6px 2px var(--highlight);
    }
</style>