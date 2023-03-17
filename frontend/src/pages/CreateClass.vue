<template>

  <!-- Back button -->
  <div id="back-items" v-motion-slide-right>
      <button id="back" @click="$router.back(-1)">
          <img :src="ArrowBack" alt="Go back to Dashboard" />
          <span> Back </span>
      </button>
  </div>
    
  <div id="create-class-container">

    <!-- Class details input forms -->
    <div id="class-details-container">
      <h2>Class Details</h2>
      <div id="class-details-input">
        
        <div id="class-name-container">
          <input type="text" id="class-name-input" placeholder="Enter class name" v-model="className">
        </div>
        <div id="class-time-container">
          <input type="text" id="class-time-input" placeholder="Enter class time" v-model="classTime">
        </div>
        <div id="class-code-container">
          <input type="text" id="class-code-input" placeholder="Enter class code" v-model="classCode">
        </div>
        <div id="room-container">
          <input type="text" id="room-input" placeholder="Enter room (optional)" v-model="room">
        </div>
        <div id="section-name-container">
          <input type="text" id="section-name-input" placeholder="Enter section (optional)" v-model="sectionName">
        </div>
      </div>
    </div>
    
    <!-- Professor details input forms -->
    <div id="professor-container">
      <h2>Professor Details</h2>
      <div id="professor-input">
        <div id="professor-name-container">
          <input type="text" id="professor-name-input" placeholder="Enter professor name" v-model="profName">
        </div>
        <div id="professor-email-container">
          <input type="text" id="professor-email-input" placeholder="Enter professor email" v-model="profEmail">
        </div>
        <div id="professor-office-container">
          <input type="text" id="professor-office-input" placeholder="Enter office location" v-model="profOffice">
        </div>
        
      </div>
    </div>

    <!-- Submit button -->
    <div v-if="classRoute" id="add-button">
      <button class="button bar" id="add-button" @click="createClass">Update Class</button>
    </div>
    <div v-else id="add-button">
      <button class="button bar" id="add-button" @click="createClass">Add New Class</button>
    </div>

  </div>

</template>

<script setup>
  import { default as axios } from 'axios';
  import ArrowBack from "/artifacts/arrowback.svg";
  import { ref, computed, onMounted } from "vue";
  import { useRoute } from 'vue-router';
  import { storeToRefs } from "pinia";
  import { useStore } from "../stores";

  const store = useStore();
  const { sessionTimer, userId, studyClass } = storeToRefs(store);
  const { updateSkin, setPageName, setStudyClass, setModal, toggleModal } = store;

  onMounted(() => {
    if(classRoute)
      setPageName("Manage Class");
    else
      setPageName("Create New Class");
  });

  // Get classRoute from URL
  let classRoute = useRoute().params.slug;
  let className, sectionName, classCode, room, classTime, profName, profEmail, profOffice;

  function createClass() {
    className = document.getElementById("class-name-input").value;
    sectionName = document.getElementById("section-name-input").value;
    classCode = document.getElementById("class-code-input").value;
    room = document.getElementById("room-input").value;
    classTime = document.getElementById("class-time-input").value;
    profName = document.getElementById("professor-name-input").value;
    profEmail = document.getElementById("professor-email-input").value;
    profOffice = document.getElementById("professor-office-input").value;


    /*
    Send data to backend. Can either be a NEW class or an UPDATE to an existing class.
    */
    const host = 'http://127.0.0.1:5000'; 
    const apiUrlNew = `/api/newclass`;
    const apiUrlUpdate = `/api/class/${classRoute}/update_meta`;
    const data = {
      className: className,
      sectionName: sectionName,
      classCode: classCode,
      room: room,
      classTime: classTime,
      profName: profName,
      profEmail: profEmail,
      profOffice: profOffice
    };

    // Update current class information
    if(classRoute){
      axios.post(host + apiUrlUpdate, data)
        .then(function (response) {
          console.log(response);
          setModal("Success", "success", response.data);
          toggleModal();
        })
        .catch(function (error) {
          console.log(error.response);
          setModal("Error", "error", error.response.data);
          toggleModal();
        });
    }
    // Create new class
    else{
      axios.post(host + apiUrlNew, data)
        .then(function (response) {
          console.log(response);
          setModal("Success", "success", response.data);
          toggleModal();
        })
        .catch(function (error) {
          console.log(error.response);
          setModal("Error", "error", error.response.data);
          toggleModal();
        });
    }
  };


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
    position: absolute;
    bottom: -1em;
    width: max-content;
  }

  .button{
    background: var(--button);
    border: 3px solid var;
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
    position: relative;
  }

  #create-class-container h2{
    display: flex;
    justify-content: left;
    padding-left: 3vw;
  }

  #create-class-container h2{
    margin-top: 3vh;
  }

  #create-class-container input{
    padding-left: 1vw;
  }

  /* Class Details Style*/

  #class-details-container{
    justify-items: flex;
  }

  #class-details-input, #professor-input{
    display: grid;
    grid-gap: 1vh 2vw;
    grid-template-columns: 50% 50%;
    padding-left: 8vw;
    padding-right: 10vw;
  }

  #class-name-container{
    width: 100%;
    grid-column: 1/3;
    grid-row: 1;
  }

  #class-name-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  #section-name-container{
    grid-column: 2/3;
    grid-row: 3;
  }

  #section-name-input{
    align-items: right;
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  #class-code-container{
    grid-column: 2/3;
    grid-row: 2;
  }

  #class-code-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  #room-container{
    grid-column: 1/2;
    grid-row: 3;
  }

  #room-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  #class-time-container{
    grid-column: 1/2;
    grid-row: 2;
  }

  #class-time-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  /*  
  Styling for the professor container. 
  Uses grids to displau them
  */

  #professor-name-container{
    grid-column: 1/3;
    grid-row: 4;
  }

  #professor-name-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  #professor-email-container{
    grid-column: 1/2;
    grid-row: 5;
  }

  #professor-email-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

  #professor-office-container{
    grid-column: 2/3;
    grid-row: 5;
  }
  
  #professor-office-input{
    width: 100%;
    height: 5vh;
    font-size: medium;
    border-radius: 1em;
    background: var(--white);
    color: var(--black);
  }

</style>