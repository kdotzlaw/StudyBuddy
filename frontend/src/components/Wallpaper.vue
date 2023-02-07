<template>
    <div id="wallpaper"></div>
    <div id="bg-gradient"></div>
</template>

<style scoped>
    #wallpaper{
        position: absolute;
        height: 100%;
        width: 100%;
        z-index: 1;
        background: var(--background);
        background-size: contain;
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