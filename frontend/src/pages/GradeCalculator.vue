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
      <div id="breakdown-table">
        <table> 
          <thead>
            <tr>
              <th id="col_one">Type Name</th>
              <th id="col_two">QTY</th>
              <th id="col_three">Percentage</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="text" id="name-input" placeholder="Quiz" v-model="username"></td>
              <td><input type="number" min="0" id="qty-input" placeholder="0" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username"> %</td>
            </tr>
            <tr>
              <td><input type="text" id="name-input" placeholder="Quiz" v-model="username"></td>
              <td><input type="number" min="0" id="qty-input" placeholder="0" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username"> %</td>
            </tr>
            <tr>
              <td><input type="text" id="name-input" placeholder="Quiz" v-model="username"></td>
              <td><input type="number" min="0" id="qty-input" placeholder="0" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username"> %</td>
            </tr>
            <tr>
              <td><input type="text" id="name-input" placeholder="Quiz" v-model="username"></td>
              <td><input type="number" min="0" id="qty-input" placeholder="0" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username"> %</td>
            </tr>
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
              <th id="col_one">Letter Grade</th>
              <th id="col_two">Max</th>
              <th id="col_three">Min</th>
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

  #breakdown-table{
    width: 70%;
    height: 80%;
    margin-left: auto;
    margin-right: auto;
    overflow-y: auto;
  }

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

  #breakdown-table th{
    top: 0;
    position: sticky;
    background-color: var(--indigo);
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

  #col_two, #col_three{
    width: 25%;
  }

  #name-input{
    width: 40%
  }

  #qty-input, #percent-input{
    width: 30%;
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

  #letter-table ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: var(--white);
    opacity: 1; /* Firefox */
  }
</style>