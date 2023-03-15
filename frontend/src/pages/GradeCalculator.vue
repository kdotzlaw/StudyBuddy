<template>
  <!-- <div class="gradeCalcPage"> -->

    <div id="back-items" v-motion-slide-right>
        <button id="back" @click="$router.back(-1)">
            <img :src="ArrowBack" alt="Go back to Dashboard" />
            <span> Back </span>
        </button>
    </div>
    
  <div id="grade-container">
    <div id="breakdown-container">
      <h2>Breakdown and Weights</h2>
      <button id="add-row" @click="createRow()"> + </button>

      <div id="breakdown-table">
        <table> 
          <thead id="breakdown-table-header">
            <tr class="grid-one">
              <th id="col-one">Name</th>
              <th id="col-two">QTY</th>
              <th id="col-three">Percentage</th>
              <th id="col-four">Delete</th>
            </tr>
          </thead>
          <tbody id="table-buddy">
            <tr class="grid-one">
              <td><input type="text" id="name-input" placeholder="Quiz" v-model="username"></td>
              <td><input type="number" min="0" id="qty-input" placeholder="0" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="percent-input" placeholder="0" v-model="username"> %</td>
              <td> <button type="button" value="Delete">Delete</button></td>
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
            <tr class="grid-two">
              <th id="col-one">Letter Grade</th>
              <th id="col-two">Max</th>
              <th id="col-three">Min</th>
            </tr>
          </thead>
          <tbody id="letter-grade-body">
            <tr class="grid-two">
              <td id="letter-grade">A+</td>
              <td><input type="number" min="0" max="100" id="max-input-A+" placeholder="100" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="min-input-A+" placeholder="90" v-model="username"> </td>
            </tr>
            <tr class="grid-two">
              <td id="letter-grade">A</td>
              <td><input type="number" min="0" max="100" id="max-input-A" placeholder="89.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="min-input-A" placeholder="80" v-model="username"> </td>
            </tr>
            <tr class="grid-two">
              <td id="letter-grade">B+</td>
              <td><input type="number" min="0" max="100" id="max-input-B+" placeholder="79.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="min-input-B+" placeholder="75" v-model="username"> </td>
            </tr>
            <tr class="grid-two"> 
              <td id="letter-grade">B</td>
              <td><input type="number" min="0" max="100" id="max-input-B" placeholder="74.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="min-input-B" placeholder="70" v-model="username"> </td>
            </tr>
            <tr class="grid-two">
              <td id="letter-grade">C+</td>
              <td><input type="number" min="0" max="100" id="max-input-C+" placeholder="69.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="min-input-C+" placeholder="65" v-model="username"> </td>
            </tr>
            <tr class="grid-two">
              <td id="letter-grade">C</td>
              <td><input type="number" min="0" max="100" id="max-input-C" placeholder="64.9" v-model="username"></td>
              <td><input type="number" min="0" max="100" id="min-input-C" placeholder="60" v-model="username"> </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div id="save-button">
      <button class="button bar" @click="update">Save Changes</button>
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
  const { updateSkin, setPageName, setStudyClass, setModal, toggleModal } = store;

  onMounted(() => {
      setPageName("Grade Calculator");
  });


  function createRow(){
    let newRow = document.createElement("tr");

    let name = document.createElement("td");
    let qty = document.createElement("td");
    let percent = document.createElement("td");
    let deleteButton = document.createElement("td");

    let nameInput = document.createElement("input");
    let qtyInput = document.createElement("input");
    let percentInput = document.createElement("input");
    let deleteButtonInput = document.createElement("button");

    newRow.classList.add("grid-one");

    nameInput.setAttribute("type", "text");
    nameInput.setAttribute("placeholder", "Quiz");

    qtyInput.setAttribute("type", "number");
    qtyInput.setAttribute("placeholder", "0");
    qtyInput.setAttribute("min", "0");

    percentInput.setAttribute("type", "number");
    percentInput.setAttribute("placeholder", "0");
    percentInput.setAttribute("min", "0");
    percentInput.setAttribute("max", "100")

    deleteButtonInput.setAttribute("type", "button");
    deleteButtonInput.innerHTML = "Delete";
    

    name.appendChild(nameInput);
    qty.appendChild(qtyInput);
    percent.appendChild(percentInput);
    deleteButton.appendChild(deleteButtonInput);

    newRow.appendChild(name);
    newRow.appendChild(qty);
    newRow.appendChild(percent);
    newRow.appendChild(deleteButton);

    percent.innerHTML += " %";

    document.getElementById("table-buddy").appendChild(newRow);
  }

  function getDataOne(){
    let table = document.getElementById("table-buddy");
    let rows = table.getElementsByTagName("tr");
    let data = [];

    for(let i = 0; i < rows.length; i++){
      let row = rows[i];
      let cols = row.getElementsByTagName("td");
      let name = cols[0].getElementsByTagName("input")[0].value;
      let qty = cols[1].getElementsByTagName("input")[0].value;
      let percent = cols[2].getElementsByTagName("input")[0].value;

      data.push({
        name: name,
        qty: qty,
        percent: percent
      });
    }

    console.log(data)

    return data;
  }

  function getDataTwo() {
    aPlus = document.getElementById("max-input-A+").value;
    a = document.getElementById("max-input-A").value;
    bPlus = document.getElementById("max-input-B+").value;
    b = document.getElementById("max-input-B").value;
    cPlus = document.getElementById("max-input-C+").value;
    c = document.getElementById("max-input-C").value;

    data = {
      aPlus: aPlus,
      a: a,
      bPlus: bPlus,
      b: b,
      cPlus: cPlus,
      c: c
    }

    console.log(data)
  }

  function update(){
    /******************************************* 
     * TODO: Update POST endpoint
     *******************************************/

     const host = 'http://127.0.0.1:5000'; 
    const apiUrl = '/api/';
    const data = getData();
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
    position: absolute;
    bottom: -1em;
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
    position: relative;
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
    display: flex;
    height: 5vh;
    justify-content: center;
  }

  tr td:nth-child(2) input, td:nth-child(3) input{
    width: 25%;
  }

  tr td:nth-child(1) input{
    width: 80%
  }

  .grid-one{
    display: grid;
    grid-template-columns: 25% 25% 25% 25%;

  }

  .grid-two{
    display: grid;
    grid-template-columns: 40% 33% 33%;
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
    width: 100%;
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
    width: 50%;
    border-radius: 5px;
    height: 3vh;
    border-style: none;
    text-align: center;
  }

  #letter-grade-container{
    width: 70%;
    height: 45%;
    margin: auto;
  }

#letter-grade-body td{
  width: 30%;
  text-align: left;
}

  #letter-table-header{
    /*background-color: var(--indigo);*/
    color: var(--white);
    text-align: center;
  }

  #letter-table ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: var(--white);
    opacity: 1; /* Firefox */
  }
</style>