<script setup>
    const props = defineProps({ 
        title: {type: String, required: false, default: "Modal Title"}
    })
</script>

<template>
    <div id="modal-inner">
        <h2>{{ title }}</h2>
        <slot />
    </div>
</template>

<style scoped>
    #modal-inner{
        height: 85%;
        width: 85%;
    }
</style>