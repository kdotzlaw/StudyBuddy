<!-- 
  Login.vue 
    Renders form fields and controls, and runs validation checks for logging in an existing account.
-->

<template>
  <div class="container">
    <form class="form" id="login">
        <div class="login-container">
          <div class="form-input-group">
            <input type="text" id="signinUsername" class="form-input" autofocus placeholder="Username" v-model="username" @keydown="checkEnter">
            <div class="form-input-error-message" v-if="usernameErrorMsg">{{ usernameErrorMsg }}</div>
          </div>
          <div class="form-input-group">
            <input type="password" id="signinPassword" class="form-input" autofocus placeholder="Password" v-model="password" @keydown="checkEnter">
            <div class="form-input-error-message" v-if="passwordErrorMsg">{{ passwordErrorMsg }}</div>
          </div>
          <button class="login-button" type="button" @click="validateForm">Log In</button>
          <p class="form-text">
            <a href="#" class="form-link" id="forgotPasswordLink">Forgot your password?</a>
            <div class="form-input-feedback-message" v-if="emailSent" >{{ emailSent }}</div>
          </p>
          <p class="form-text">

              <!-- Switch to Register form -->
              <a class="form-link" id="linkCreateAccount">Don't have an account? Create account</a>

          </p>
        </div>
    </form>
  </div>
</template>

<script setup>
  import { default as axios } from 'axios';
  import{ ref } from "vue";
  import validate from "../logic/validate";
  import { useStore } from "../stores";
  import { storeToRefs } from "pinia";

  let username, password;
  const usernameErrorMsg = ref('');
  const passwordErrorMsg = ref('');
  const emailSent = ref('');

  const store = useStore();
  const { setModal, toggleModal, loginUser } = store;


  function checkLinks(){
    setTimeout(() => {
    const forgotPasswordLink = document.getElementById("forgotPasswordLink");
    forgotPasswordLink.addEventListener("click", () => {
      emailSent.value = 'Instructions to reset your password has been sent to your email!';
    });
   }, 500);

    setTimeout(() => {
      const linkCreateAccount = document.getElementById("linkCreateAccount");
      linkCreateAccount.addEventListener("click", () => {
        setModal("Create Account", "register");
        toggleModal();
      });
    }, 500);
  }

  checkLinks();

  // Detect when ENTER key pressed to submit form
  function checkEnter(event){
    if(event.key == "Enter")
        validateForm();
    event.stopImmediatePropagation();
  }

  /* validateForm
   *   Runs all validation checks on form submit, and sends data to login authentication endpoint when validations pass.
   *   Display notes for validation failure, or show authentication success/error modal after form submit.
   */
  function validateForm() {
    let username = document.getElementById("signinUsername").value;
    let password = document.getElementById("signinPassword").value;

    var userNameCheck = false;
    var passwordErrorCheck = true;

    // Validate check username
    if (validate.isInputEmpty(username)) {
      usernameErrorMsg.value = 'Username is required';
      userNameCheck = true;
    } else {
      usernameErrorMsg.value = '';
      userNameCheck = false;
    }

    // Validate check password
    if (validate.isInputEmpty(password)) {
      passwordErrorMsg.value = 'Password is required';
      passwordErrorCheck = true;
    } else {
      passwordErrorMsg.value = '';
      passwordErrorCheck = false;
    }

    // Validation checks pass; Send data to server endpoint
    if (!userNameCheck && !passwordErrorCheck) {
      const host = 'http://127.0.0.1:5000'; 
      const apiUrl = '/api/login';
      const data = {
        username: username,
        password: password
      };
      axios.post(host + apiUrl, data)
      .then(function (response) {
        console.log(response.headers['set-cookie']);
        loginUser(username);
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
</script>

<style>
body {
  --color-primary: #4241A9;
  --color-primary-dark: #5A6F9C;
  --color-secondary: #ffffff;
  --color-error: #cc3333;
  --color-success: #4bb544;
  --border-radius: 4px;

  margin: 0;

  display: flex;

  font-size: 18px;
}

.container {
  margin: 1rem;
  padding: 1rem;
  border-radius: var(--border-radius);
  
}

.container,
.form-input,
.login-button {
  font: 500 1rem 'Quicksand', sans-serif;
}

.login-container{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 25vw;
}

.form > *:first-child {
  margin-top: 0;
}

.form > *:last-child {
  margin-bottom: 0;
}

.form-title {
  margin-bottom: 2rem;
  text-align: center;
}

.form-message {
  text-align: center;
  margin-bottom: 1rem;
}

.form-message--success {
  color: var(--color-success);
}

.form-message--error {
  color: var(--color-error);
}

.form-input-group {
  margin-bottom: 1rem;
}

.form-input {
  display: block;
  width: 100%;
  padding: 0.75rem;
  box-sizing: border-box;
  border-radius: var(--border-radius);
  border: 1px solid #dddddd;
  outline: none;
  background: #eeeeee;
  transition: background 0.2s, border-color 0.2s;
}

.form-input:focus {
  border-color: var(--color-primary);
  background: #ffffff;
}

.form-input-error-message {
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: var(--color-error);
}

.form-input-feedback-message {
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: var(--color-success);
}

.login-button {
  width: 100%;
  padding: 1rem 2rem;
  font-weight: bold;
  font-size: 1.1rem;
  color: #ffffff;
  border: none;
  border-radius: var(--border-radius);
  outline: none;
  cursor: pointer;
  background: var(--color-primary);
}

.login-button:hover {
  background: var(--color-primary-dark);
}

.login-button:active {
  transform: scale(0.98);
}

.form-text {
  text-align: center;
}

.form-link {
  color: var(--color-secondary);
  text-decoration: none;
  cursor: pointer;
}

.form-link:hover {
  text-decoration: underline;
}
</style>
