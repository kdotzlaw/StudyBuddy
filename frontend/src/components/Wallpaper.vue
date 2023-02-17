<!-- 
  Wallpaper.vue 
    Renders appearance of page backgrounds based on selected UI skin.
-->

<script setup>
    import { storeToRefs } from "pinia";
    import { useStore } from "../stores";
    const store = useStore();
    const { uiSkin } = storeToRefs(store);
</script>

<template>
    <div id="wallpaper" :class=uiSkin  />
    <div id="bg-gradient" :class=uiSkin />
</template>

<style scoped>
    #wallpaper{
        position: absolute;
        height: 100%;
        width: 100%;
        z-index: 1;
        background-size: cover;
        background-repeat: no-repeat;
    }

    #bg-gradient{
        position: absolute;
        height: 100%;
        width: 100%;
        z-index: 2;
    }
</style>