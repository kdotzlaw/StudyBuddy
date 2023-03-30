<!-- 
  AddRequirement.vue
    route: /class/${classRoute}/newtask
           /class/${classRoute}/task/${reqName}/edit
           /class/${classRoute}/task/${reqName}/complete

    Modal for adding a new requirement
-->
<template>
  <div id="add-req-container">
    <div id="name-req">
      <h3>Requirement Name</h3>
      <input type="text" id="name-req-input" placeholder="Enter requirement name" v-model="reqName" @keydown="checkEnter">
    </div>
    <div id="grade-req">
      <h3>Weight</h3>
      <input type="text" id="grade-req-input" placeholder="%" v-model="gradeReq" @keydown="checkEnter">
    </div>
    <div id="date-req">
      <h3>Due Date</h3>
      <input type="datetime-local" id="date-req-input" placeholder="" v-model="reqDate">
    </div>
    <div v-if="edit" id="finish-req">
      <h3>Grade Received</h3>
      <input type="number" id="finish-req-input" placeholder="90" v-model="finishReq" @keydown="checkEnter">
    </div>

    <div v-if="edit" id="delete-req">
      <button class="button bar" id="delete-button" @click="deleteReq()"> Delete</button>
    </div>

    <div v-if="edit" id="add-button-outer">
      <button class="button bar" id="add-button" @click="addToCalendar()">Save changes</button>
    </div>
    <div v-else id="add-button-outer">
      <button class="button bar" id="add-button" @click="addToCalendar()">Add to calendar</button>
    </div>
  </div>


</template>

<script setup>
  import { default as axios } from 'axios';
  import { useRoute } from 'vue-router';
  import { storeToRefs } from "pinia";
  import { ref, computed } from "vue";
  import { useStore } from "../stores";

  const store = useStore();
  const {setModal, toggleModal} = store;

  const props = defineProps({ 
    edit: {type: Boolean, required: false, default: false},
  })
  
  let classRoute = useRoute().params.slug;
  let reqName, gradeReq, reqDate, finishReq;

  /*  checkEnter
   *    Detect when ENTER key pressed to submit form
   */
  function checkEnter(event){
    if(event.key == "Enter")
        addToCalendar();
    event.stopImmediatePropagation();
  }

  /*  addToCalendar
   *    Add requirement to calendar
   */
  function addToCalendar(){
    reqName = document.getElementById("name-req-input").value;

    if(reqName){
      gradeReq = document.getElementById("grade-req-input").value;
      reqDate = document.getElementById("date-req-input").value;
      if(reqDate)
        reqDate = new Date(reqDate).toISOString();
      else
        reqDate = new Date(Date.now()).toISOString();

      const host = 'http://127.0.0.1:5000'; 
      const apiUrlNew = `/api/class/${classRoute}/newtask`;
      const apiUrlUpdate = `/api/class/${classRoute}/task/${reqName}/edit`;
      const apiUrlComplete = `/api/class/${classRoute}/task/${reqName}/complete`;
      let data = {
        classname: classRoute,
        taskname: reqName,
        weight: gradeReq,
        deadline: reqDate,
      };
      let updateData = {
        classname: classRoute,
        newname: reqName,
        newdeadline: reqDate,
        newweight: gradeReq
      };
      
      // Checks to see if they are editting the requirement
      let complete = false;
      if(props.edit){
        finishReq = document.getElementById("finish-req-input").value;
        if(finishReq.length > 0){
          data.grade = finishReq;
          complete = true;
        }
      }

      // Mark current task as finished
      if(props.edit && complete){
        axios.post(host + apiUrlComplete, data)
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
      // Update current task information
      else if (props.edit && !complete){
        axios.post(host + apiUrlUpdate, updateData)
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
      // Create new task
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
    }
    
  }

  /*  deleteReq
   *    Delete requirement from calendar
   */
  function deleteReq(){
    reqName = document.getElementById("name-req-input").value;

    if(reqName){
      const host = 'http://127.0.0.1:5000'; 
      const apiUrl = `/api/class/${classRoute}/task/${reqName}/delete`;

      let data = {
        classname: classRoute,
      };

      if(props.edit){
        axios.post(host + apiUrl, data)
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
    }
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

#delete-button{
  margin-left: 0; 
  margin-right: 60%;
  position: absolute;
  bottom: -1em;
  left: 6em;
  width: max-content;
  transform: scale(1.2);
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