<script setup>
  import { ref } from "vue"

  const props = defineProps({ 
    text: {type: String, required: false, default: "Button"}
  })

  function clickButt(){ yayText.value += "Yay!<br>" }
  const yayText = ref("")
</script>

<template>
  <button @click="clickButt"> {{ props.text }} </button>
  <div v-html="yayText"></div>
</template>