<template>
  <!-- <div class="gradeCalcPage"> -->

    <div id="back-items" v-motion-slide-right>
      <router-link to="/class">
          <button id="back">
              <img :src="ArrowBack" alt="Go back to Dashboard" />
              <span> Back </span>
          </button>
      </router-link>
    </div>
    
  <!-- </div> -->
  <div id="grade-container">
    <div id="breakdown-container">
      <h2>Breakdown and Weights</h2>
    </div>
    
    <div id="letter-grade-container">
      <h2>Letter Grade Breakdown</h2>
    </div>

    <div id="save-button">
      <button class="button bar">
        Save Changes
      </button>
    </div>

  </div>

</template>

<script setup>
  import ArrowBack from "/artifacts/arrowback.svg";
  import { ref, computed, onMounted } from "vue";
  import { storeToRefs } from "pinia";
  import { useStore } from "../stores";


  const store = useStore();
  const { sessionTimer, userId, studyClass } = storeToRefs(store);
  const { updateSkin, setPageName, setStudyClass } = store;

  onMounted(() => {
      setPageName("Grade Calculator");
    });

</script>

<style>

  #gradeCalcPage{

  }

  #title h1{
    font-size: 72px;
    letter-spacing: 5px;
    margin: 0;
    align-items: center;
    font-weight: 400;
    line-height: 40px;
    align-items: center;
  }
  #back-items{
    position: absolute;
    z-index: 4;
    display: flex;
    align-items: center;
  }

  #back{
    display: flex;
    align-items: center;
    background: none;
    outline: none;
  }

  #back img, #study-ctrl{
    height: 40%;
    width: 40%;
  }

  #back span{
    font-weight: 800;
    font-size: 20px;
    color: var(--gold);
    margin-left: 5%;
  }

  #save-button{
    margin-left: 75%; 
    margin-right: 0;
  }

  .button{
    background: var(--button);
    border: 3px solid var(--gold);
    box-shadow: inset 0.2em 0.2em 0.6em rgba(0,0,0,0.4);
    display: grid;
    justify-items: center;
    align-items: center;
    color: var(--gold);
    border-radius: 1em;
    font-family: 'Croissant One', cursive;
  }

  .button:hover{
      transition: 0.3s;
      background: var(--button-shade);
  }

  .bar{
    padding: 0.7em 2.3em 0.7em 2.3em;
  }

  #grade-container{
    width: 70%;
    height: 90%;


    background: var(--indigo);
    border: 3px solid var(--gold);
    border-radius: 2em;
    box-shadow: inset 0.2em 0.2em 0.6em rgba(0,0,0,0.4);
    margin: auto;
    
  }

  #grade-container h2{
    display: flex;
    justify-content: center;
  }

  #breakdown-container{
    width: 70%;
    height: 45%;
    background-color: red;
    margin: auto;
  }

  #letter-grade-container{
    width: 70%;
    height: 45%;
    background-color:  blue;
    margin: auto;
  }

</style>