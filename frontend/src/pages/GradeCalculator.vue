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
    
  <div id="grade-container">
    <div id="breakdown-container">
      <h2>Breakdown and Weights</h2>

      <!-- <div id="breakdown-input">
        <h3 id="subtitle">New Assesment:</h3>
        <label for="name-input">Name: </label>
        <input type="text" id="name-input" placeholder="Quiz" v-model="username">
        <label for="qty-input">QTY: </label>
        <input type="number" min="0" id="qty-input" placeholder="0" v-model="username">
        <label for="percent-input">Percent: </label>
        <input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username">
        <button class="button bar">Add</button>
      </div> -->

      <div id="breakdown-table">
        <table> 
          <thead id="breakdown-table-header">
            <tr>
              <th id="col-one">Name</th>
              <th id="col-two">QTY</th>
              <th id="col-three">Percentage</th>
              <th id="col-four">Delete</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="text" id="name-input" placeholder="Quiz" v-model="username"></td>
              <td><input type="number" min="0" id="qty-input" placeholder="0" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username"> %</td>
            </tr> 
          </tbody>
        </table>
      </div>
      
    </div>
    
    <div id="letter-grade-container">
      <h2>Letter Grade Breakdown</h2>
      <div id="letter-table">
        <table> 
          <thead id="letter-table-header">
            <tr>
              <th id="col-one">Letter Grade</th>
              <th id="col-two">Max</th>
              <th id="col-three">Min</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>A+</td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="100" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="90" v-model="username"> </td>
            </tr>
            <tr>
              <td>A</td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="89.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="80" v-model="username"> </td>
            </tr>
            <tr>
              <td>B+</td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="79.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="75" v-model="username"> </td>
            </tr>
            <tr>
              <td>B</td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="74.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="70" v-model="username"> </td>
            </tr>
            <tr>
              <td>C+</td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="69.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="65" v-model="username"> </td>
            </tr>
            <tr>
              <td>C</td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="64.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="max-input" placeholder="60" v-model="username"> </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div id="save-button">
      <button class="button bar">Save Changes</button>
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
    width: 50%;
    height: 90%;
    background: var(--indigo);
    border: 3px solid var(--border-gold);
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
    margin: auto;
  }

  #grade-container h2,
  #grade-container h3{
    padding: 0;
    margin:0;
  }

  #grade-container h2{
    margin-top: 2vh;
  }

  /* Overall Table Style*/
  table{
    width: 100%;
    border-collapse: collapse;
  }

  td{
    margin-left: auto;
    margin-right: auto;
    text-align: center;
  }

  tr{
    height: 5vh;
    justify-content: center;
  }

  #col-two, #col-three{
    width: 25%;
  }

  #name-input{
    width: 80%
  }

  #qty-input, #percent-input{
    width: 20%;
  }

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

  /* Breakdown Table Style*/

  #breakdown-table{
    width: 70%;
    height: 80%;
    margin-left: auto;
    margin-right: auto;
    overflow-y: auto;
  }

  #breakdown-input input{
    margin-right: 1.5vw;
  }

  #breakdown-table th{
    top: 0;
    position: sticky;
    background-color: var(--indigo);
  }

  #breakdown-table-header #col-one{
    width: 35%;
  }

  /* Letter Grade Table Style*/

  #letter-table{
    width: 70%;
    height: 80%;
    margin-left: auto;
    margin-right: auto;
    background-color: var(--textbox-dark);
    overflow-y: auto;
  }

  #letter-table tbody{
    overflow: auto;
  }

  #letter-table th{
    top: 0;
    position: sticky;
    background-color: var(--textbox-dark);
  }

  #letter-grade-container input{
    font: 500 1rem 'Quicksand', sans-serif;
    border-radius: 5px;
    height: 3vh;
    border-style: none;
  }

  #letter-grade-container{
    width: 70%;
    height: 45%;
    margin: auto;
  }

  #letter-table-header{
    /*background-color: var(--indigo);*/
    color: var(--white);
  }

  #letter-table ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: var(--white);
    opacity: 1; /* Firefox */
  }
</style>