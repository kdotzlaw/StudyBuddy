<template>
  <div id="add-req-container">
    
    <div id="name-req">
      <h3>Requirement Name</h3>
      <input type="text" id="name-req-input" placeholder="Enter requirement name" v-model="reqName">
    </div>
    <div id="grade-req">
      <h3>Letter Goal</h3>
      <input type="text" id="grade-req-input" placeholder="A" v-model="gradeReq">
    </div>
    <div id="date-req">
      <h3>Due Date</h3>
      <input type="datetime-local" id="date-req-input" placeholder="" v-model="reqDate">
    </div>
    <div v-if="edit" id="finish-req">
      <h3>Grade Received</h3>
      <input type="number" id="finish-req-input" placeholder="90" v-model="finishReq">
    </div>

    <div id="add-button-outer">
      <button class="button bar" id="add-button" @click="addToCalendar()">Add to calendar</button>
    </div>

  </div>


</template>

<script setup>
  import { storeToRefs } from "pinia";
  import { ref, computed } from "vue";
  import { useStore } from "../stores";

  const store = useStore();
  const {setModal, toggleModal} = store;

  const props = defineProps({ 
    edit: {type: Boolean, required: false, default: false}
  })
  
  let reqName, gradeReq, reqDate, finishReq;

  function addToCalendar(){
    reqName = document.getElementById("name-req-input").value;
    gradeReq = document.getElementById("grade-req-input").value;
    reqDate = document.getElementById("date-req-input").value;
    if(props.edit)
      finishReq = document.getElementById("finish-req-input").value;

    /******************************************* 
     * TODO: Update POST endpoint
     *******************************************/

    const host = 'http://127.0.0.1:5000'; 
    const apiUrl = '/api/';
    const data = {
      reqName: reqName,
      gradeReq: gradeReq,
      reqDate: reqDate,
    };
    console.log(data);
    fetch(host + apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      mode: 'no-cors',
      body: JSON.stringify(data),
      credentials: 'include'
    })
      .then(response => response.text())
      .then(data => {
        setModal("Success", "success", data);
        toggleModal();
      })
    .catch(error => {
      console.log(error);
    });
  }

</script>


<style>

#add-req-container{
  height: 100%;
  width: 100%;
  justify-items: flex;
  display: grid;
  grid-template-columns: 65% 35%;
}

#add-req-container input{
  text-align: center;
}

#name-req, #date-req{
  margin-left: 5vw;
}

#name-req{
  width: 70%;

  grid-column: 1;
  grid-row: 1;
}

#grade-req{
  width: 60%;

  grid-column: 2;
  grid-row: 1;

  text-align: center;
}

#finish-req{
  width: 100%;

  grid-column: 2;
  grid-row: 2;

  text-align: center;
}

#date-req{
  width: 70%;

  grid-column: 1;
  grid-row: 2;
}

#name-req-input{
  width: 85%;
  height: 5vh;
  font-size: medium;
  border-radius: 1em;
  background: var(--white);
  color: var(--black);
}

#grade-req-input, #finish-req-input{
  width: 40%;
  height: 5vh;
  font-size: medium;
  border-radius: 1em;
  background: var(--white);
  color: var(--black);
}

#date-req-input{
  width: 85%;
  height: 5vh;
  font-size: medium;
  border-radius: 1em;
  background: var(--white);
  color: var(--black);
}

/* Button style*/
#add-button{
  margin-left: 70%; 
  margin-right: 0;
  position: absolute;
  bottom: -0.5em;
  right: 5em;
  width: max-content;
  transform: scale(1.15);
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

</style>