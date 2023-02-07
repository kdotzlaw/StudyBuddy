<script setup>
  import "./global.css";
  import { ref } from "vue";
  import Header from "./components/Header.vue";
  import Dashboard from "./pages/Dashboard.vue";
  import Wallpaper from "./components/Wallpaper.vue";
  import Modal from "./components/Modal.vue";
  import YayButton from "./components/Button.vue";

  const isModalOpen = ref(false);
  function openModal(){
    isModalOpen.value = !isModalOpen.value;
  }
</script>

<template>
  <Header />
  <div id="workspace">
    <button @click="openModal">Toggle the modal</button>
    <Dashboard>
      <YayButton text="Click here to print 'Yay'" />
    </Dashboard>
  </div>
  <Wallpaper />
  <div v-if="isModalOpen" id="modal">
    <Modal title="Success!">
      <p>A badoogie doogie</p>
      <img src="/assets/title_sq.png" :style="`height:4em; width:4em;`" alt="Study Buddy title" /> I am passed through a slot!
    </Modal>
  </div>
</template>

<style scoped>
  #workspace{
    position: absolute;
    z-index: 8;
    margin: 15vh 0 0 3em;
    height: 85vh;
    width: 96vw;
    overflow-y: scroll;
  }

  #modal{
    position: fixed;
    z-index: 20;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }

  #modal{
      background: var(--box);
      height: 60vh;
      width: 40vw;
      display: grid;
      justify-items: center;
      align-items: center;
  }
</style>