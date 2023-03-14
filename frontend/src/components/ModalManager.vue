<!-- 
  ModalManager.vue 
    Render internal contents of a modal. ModalManager can be passed 2 prop types: a contentId to render a 
    preset component or element from the v-if conditionals, and/or a renderString for custom HTML rendering.
-->

<script setup>
    import SuccessIcon from "/artifacts/success.svg";
    import ErrorIcon from "/artifacts/error.svg";
    import Login from "./Login.vue";
    import Register from "./Register.vue"; 
    import Settings from "./Settings.vue";
    import AddRequirement from "./AddRequirement.vue";


    const props = defineProps({ 
        contentId: {type: String, required: false, default: null},
        renderString: {type: String, required: false, default: ""}
    })
</script>

<template>

    <!-- Content presets -->
    <div v-if="contentId=='success'" class="form-ctr">
        <img :src="SuccessIcon" alt="Success Party hat!" :style="`height:6em;width:6em;justify-self:center;`" />
    </div>
    <div v-else-if="contentId=='error'" class="form-ctr">
        <img :src="ErrorIcon" alt="Error, snap" :style="`height:6em;width:6em;justify-self:center;`" />
    </div>
    <div v-else-if="contentId=='register'" class="form-ctr">
        <Register/>
    </div>
    <div v-else-if="contentId=='login'" class="form-ctr">
        <Login/>
    </div>
    <div v-else-if="contentId=='settings'" class="form-ctr">
        <Settings/>
    </div>
    <div v-else-if="contentId=='addRequirement'" class="form-ctr">
        <AddRequirement />
    </div>
    <div v-else-if="contentId=='editRequirement'" class="form-ctr">
        <AddRequirement :edit="true" />
    </div>

    <!-- HTML render -->
    <div id="renderString" v-html="renderString"/>

</template>

<style scoped>
    .form-ctr{
        height: inherit;
        width: 100%;
        display: grid;
    }

    #renderString{
        font-size: 120%;
    }
</style>