<!-- 
  App.vue 
    Application-level component to define structure, contain, and conditionally mount layout components and page routes.    
-->

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

  /* updateTimer
   *   Manages the time reflected on all timer displays based on absolute date-time calculations returned by Timer class
   *   Polls and refreshes time display on reasonable interval(0.5 seconds) to ensure timer accuracy and maintain good app performance
   */
  function updateTimer(){
    if(sessionTimer.value){
      let elapsed = sessionTimer.value.getTime();
      setStudyTime(parseInt(elapsed/1000));
    }
  }
  setInterval(updateTimer, 500)
</script>

<template>
  <Header />
  
  <div id="workspace">
    <router-view></router-view>
  </div>
  <Wallpaper />
  <div v-if="isModalOpen" id="modal-ctr" v-motion-pop>
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