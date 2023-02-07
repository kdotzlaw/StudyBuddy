<script setup>
  import "./global.css";
  import { storeToRefs } from "pinia";
  import Header from "./components/Header.vue";
  import Dashboard from "./pages/Dashboard.vue";
  import Wallpaper from "./components/Wallpaper.vue";
  import Modal from "./components/Modal.vue";
  import YayButton from "./components/Button.vue";
  import { useStore } from "./stores";

  const store = useStore();
  const { toggleModal } = store;
  const { isModalOpen } = storeToRefs(store);
</script>

<template>
  <Header />
  <div id="workspace">
    <button @click="toggleModal">Toggle the modal</button>
    <Dashboard>
      <YayButton text="Click here to print 'Yay'" />
    </Dashboard>
  </div>
  <Wallpaper />
  <div v-if="isModalOpen" id="modal-ctr">
    <Modal title="Success!">
      <p>Click anywhere outside modal to close</p>
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

  #modal-ctr{
    position: fixed;
    z-index: 20;
    height: 100vh;
    width: 100vw;
  }
</style>