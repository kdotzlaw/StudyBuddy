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
    
  <div id="create-class-container">
    <div id="class-details-container">
      <h2>Class Details</h2>
      <div id="class-details-input">
        <input type="text" id="class-name-input" placeholder="Enter class name" v-model="username">
      </div>
    </div>
    
    <div id="professor-container">
      <h2>Professor Details</h2>
      <div id="professor-input">
        <input type="text" id="class-name-input" placeholder="Enter class name" v-model="username">
      </div>
    </div>

    <div id="add-button">
      <button class="button bar">Add New Class</button>
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

  #add-button{
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

  /* Overall style*/

  #create-class-container{
    width: 50%;
    height: 90%;
    background: var(--indigo);
    border: 3px solid var(--border-gold);
    border-radius: 2em;
    box-shadow: inset 0.2em 0.2em 0.6em rgba(0,0,0,0.4);
    margin: auto;
  }

  #create-class-container h2{
    display: flex;
    justify-content: left;
    padding-left: 3.5vw;
  }

  #create-class-container h2{
    margin-top: 3vh;
  }

  #create-class-container input{
    padding-left: 1vw;
  }

  /* Class Details Style*/
  #class-details-input, #professor-input{
    display: flex;
    justify-content: center;
  }

  #class-name-input{
    width: 50%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }



/*

  #min-input, #max-input{
    background-color: var(--box);
    color: var(--white);
    text-align: center;
  }

  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  #letter-table ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ 
    color: var(--white);
    opacity: 1; /* Firefox 
  }

  */
</style>