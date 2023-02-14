<script setup>
    import Login from "./Login.vue";
    import Register from "./Register.vue"; 
    import Settings from "./Settings.vue";

    const props = defineProps({ 
        contentId: {type: String, required: false, default: null},
        renderString: {type: String, required: false, default: ""}
    })
</script>

<template>
    <div v-if="contentId=='register'" class="form-ctr">
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