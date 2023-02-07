<script setup>
    import { useStore } from "../stores";

    const store = useStore();
    const { toggleModal } = store;

    const props = defineProps({ 
        title: {type: String, required: false, default: "Modal Title"}
    })
</script>

<template>
    <div id="modal">
        <div id="modal-inner">
            <h2>{{ title }}</h2>
            <slot />
        </div>
    </div>
    <div id="modal-overlay" @click="toggleModal"></div>
</template>

<style scoped>
    #modal-overlay{
        position: absolute;
        height: 100%;
        width: 100%;
        background: rgba(0,0,0,0.3);
        cursor: pointer;
    }

    #modal{
        position: absolute;
        z-index: 21;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        background: var(--box);
        height: 60vh;
        width: 40vw;
        display: grid;
        justify-items: center;
        align-items: center;
    }

    #modal-inner{
        height: 85%;
        width: 85%;
    }
</style>