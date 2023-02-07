<script setup>
    const props = defineProps({ 
        skin: {type: String, required: false, default: "skin-default"}
    })
</script>

<template>
    <div id="wallpaper" :class=props.skin  />
    <div id="bg-gradient" />
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
        background: linear-gradient(to bottom, rgba(0,0,0,0) 40%, var(--indigo) 70%);
    }
</style>