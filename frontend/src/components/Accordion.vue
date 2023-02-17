<!-- 
  Accordion.vue 
    Accordion component that displays a title and collapsible body slot.
-->

<script setup>
    import ArrowToggle from "/artifacts/arrowtoggle.svg";
    import { ref } from "vue";

    const props = defineProps({ 
        title: {type: String, required: false, default: "Option Name"},
        toggled: {type: Boolean, required: false, default: true}
    })

    // Toggle or collapse Accordion
    const toggled = ref(props.toggled);
    function toggle(){
        toggled.value = !toggled.value;
    }
</script>

<template>

    <!-- Accordion head -->
    <div v-if="toggled" class="accordion-head" @click="toggle" :style="`border-bottom-left-radius:0;border-bottom-right-radius:0;border-bottom-style:none;`">
        <h2> {{ title }} </h2>
        <button class="turnup" :style="`background:url(${ArrowToggle});`" />
    </div>
    <div v-else class="accordion-head" @click="toggle">
        <h2> {{ title }} </h2>
        <button :style="`background:url(${ArrowToggle});`" />
    </div>

    <!-- Accordion body -->
    <div v-if="toggled" class="accordion-body">
        <div class="hr" />
        <slot>
            No content provided under this slot.
        </slot>
    </div>
    
</template>

<style scoped>
    .accordion-head{
        width: 30vw;
        background: var(--box);
        padding: 0.5em 3em 0.5em 2em;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 1em;
        border: 2px solid var(--gold);
        box-shadow: inset 0.3em 0.3em 0.5em rgba(0,0,0,0.4);
        margin-top: 4vh;
    }

    .accordion-head button{
        height: 1.6em;
        width: 1.6em;
        background-size: contain !important;
        background-repeat: no-repeat !important;
    }

    .accordion-body{
        width: 30vw;
        background: var(--box);
        padding: 0 2em 2em 3em;
        border-bottom-left-radius: 1em;
        border-bottom-right-radius: 1em;
        border: 2px solid var(--gold);
        border-top-style: none;
    }

    .hr{
        width: 100%;
        height: 1px;
        background: var(--button-disabled);
    }

    .turnup{
        transform: rotate(180deg);
    }
</style>