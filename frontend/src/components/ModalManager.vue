<script setup>
    import SuccessIcon from "/artifacts/success.svg";
    import ErrorIcon from "/artifacts/error.svg";
    import Login from "./Login.vue";
    import Register from "./Register.vue"; 
    import Settings from "./Settings.vue";

    const props = defineProps({ 
        contentId: {type: String, required: false, default: null},
        renderString: {type: String, required: false, default: ""}
    })
</script>

<template>
    <div v-if="contentId=='success'" class="form-ctr">
        <img :src="SuccessIcon" alt="Success Party hat!" :style="`height:6em;width:6em;`" />
    </div>
    <div v-else-if="contentId=='error'" class="form-ctr">
        <img :src="ErrorIcon" alt="Error, snap" :style="`height:6em;width:6em;`" />
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
    <div v-html="renderString"/>
</template>

<style scoped>
    .form-ctr{
        height: inherit;
        width: inherit;
    }
</style>