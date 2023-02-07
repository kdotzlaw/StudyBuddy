<script setup>
  import "./global.css"
  import Button from "./components/Button.vue"
  import Header from "./components/Header.vue"
</script>

<template>
  <Header />
  <h2>Calendar Overview</h2>
  <h3>Current Quests</h3>
  <p class="delius">You have an assignment due tomorrow for COMP2080!</p>
  <Button text = "Vue site is up!" />
</template>