<script setup>
  import "./global.css";
  import { storeToRefs } from "pinia";
  import Header from "./components/Header.vue";
  import Dashboard from "./pages/Dashboard.vue";
  import Wallpaper from "./components/Wallpaper.vue";
  import Modal from "./components/Modal.vue";
  import YayButton from "./components/Button.vue";
  import Timer from "./logic/timer";
  import { useStore } from "./stores";

  import Login from "./components/Login.vue"
  import Register from "./components/Register.vue"

  const store = useStore();
  const { isModalOpen, modalTitle, modalContent, uiSkin } = storeToRefs(store);

  // Globals
  let userId = "user123";

  // Create Timer class
  let sessionTimer = new Timer(userId, "COMP2080", 0);
  sessionTimer.start();
</script>

<template>
  <Header />
  <div id="workspace">
    <Dashboard>
      <YayButton text="Click here to print 'Yay'" />
    </Dashboard>
   
  </div>
  <Wallpaper :skin=uiSkin />
  <div v-if="isModalOpen" id="modal-ctr">
    <Modal :title="modalTitle">
      <!-- <div v-html="modalContent"></div> -->
      <Login></Login>
      <!-- <Register></Register> -->
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