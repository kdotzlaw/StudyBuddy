<script setup>
  import "./global.css";
  import { storeToRefs } from "pinia";
  import Header from "./components/Header.vue";
  import Dashboard from "./pages/Dashboard.vue";
  import Wallpaper from "./components/Wallpaper.vue";
  import Modal from "./components/Modal.vue";
  import ModalManager from "./components/ModalManager.vue";
  import { useStore } from "./stores";

  import Login from "./components/Login.vue"
  import Register from "./components/Register.vue"

  const store = useStore();
  const { setStudyTime } = store;
  const { sessionTimer, isModalOpen, modalTitle, modalContent, modalRender } = storeToRefs(store);
  
  // Refresh timer every 0.5 second
  setInterval(updateTimer, 500)
  function updateTimer(){
    if(sessionTimer.value){
      let elapsed = sessionTimer.value.getTime();
      setStudyTime(parseInt(elapsed/1000));
    }
  }
</script>

<template>
  <Header />
  
  <div id="workspace">
    <router-view></router-view>
  </div>
  <Wallpaper />
  <div v-if="isModalOpen" id="modal-ctr">
    <Modal :title="modalTitle">
      <ModalManager :contentId="modalContent" :renderString="modalRender" />
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