<template>
  <div>
    <form class="form " id="createAccount">
      <div class="register-container">
        <div class="form-input-group">
          <input type="text" id="signupUsername" class="form-input" autofocus placeholder="Username" v-model="username">
          <div class="form-input-error-message" v-if="usernameErrorMsg">{{ usernameErrorMsg }}</div>
        </div>
        <div class="form-input-group">
            <input type="text" id="signupEmail" class="form-input" autofocus placeholder="Email Address" v-model="email">
            <div class="form-input-error-message" v-if="emailErrorMsg">{{ emailErrorMsg }}</div>
        </div>
        <div class="form-input-group">
            <input type="password" id="signupPassword" class="form-input" autofocus placeholder="Password" v-model="password">
            <div class="form-input-error-message" v-if="passwordErrorMsg">{{ passwordErrorMsg }}</div>
        </div>
        <div class="form-input-group">
            <input type="password" id="signupPasswordConfirm" class="form-input" autofocus placeholder="Confirm password" v-model="confirmPassword">
            <div class="form-input-error-message" v-if="confirmpasswordErrorMsg">{{ confirmpasswordErrorMsg }}</div>
        </div>
        <button class="register-button" type="button" @click="validateForm">Register</button>
        <p class="form-text">
            <!-- <a class="form-link" href="./" id="linkLogin">Already have an account? Sign in</a> -->
        </p>
      </div>
    </form>
  </div>
</template>

<script setup>
  import{ ref } from "vue"
  import validate from "../logic/validate"

  const usernameErrorMsg = ref('');
  const emailErrorMsg = ref('');
  const passwordErrorMsg = ref('');
  const confirmpasswordErrorMsg = ref('');

  function validateForm() {
    let username = document.getElementById("signupUsername").value;
    let email = document.getElementById("signupEmail").value;
    let password = document.getElementById("signupPassword").value;
    let confirmPassword = document.getElementById("signupPasswordConfirm").value;

    var userNameValid = true;
    var emailValid = true;
    var passwordErrorValid = true;
    var passwordConfirmErrorValid = true;
    var passwordLengthValid = true;

    if (validate.isInputEmpty(username)) {
      usernameErrorMsg.value = 'Username is required';
      userNameValid = false;
    } else {
      usernameErrorMsg.value = '';
      userNameValid = true;
    }

    if (validate.isInputEmpty(email)) {
      emailErrorMsg.value = 'Email is required';
      emailValid = false;
    } else {
      emailErrorMsg.value = '';
      emailValid = true;
    }

    if (validate.isInputEmpty(password)) {
      passwordErrorMsg.value = 'Password is required';
    } else if(isValidPassword(password)){
      passwordErrorMsg.value = 'Password length must be more than 8 or more characters';
      passwordErrorValid = false;
    } else {
      passwordErrorMsg.value = '';
      passwordErrorValid = true;
    }

    if (validate.isInputEmpty(confirmPassword)) {
      confirmpasswordErrorMsg.value = 'Confirm password is required';
      passwordConfirmErrorValid = false;
    } else {
      confirmpasswordErrorMsg.value = '';
      passwordConfirmErrorValid = true;
    }

    if(passwordErrorValid && !(password == confirmPassword) && !validate.isInputEmpty(confirmPassword)){
      passwordErrorMsg.value = 'Password does not match';
      confirmpasswordErrorMsg.value = 'Password does not match';
      passwordLengthValid = false;
    } else{
      passwordLengthValid = true;
    }

    if (userNameValid && emailValid && passwordErrorValid && passwordConfirmErrorValid && passwordLengthValid) {
      console.log("Gotta fetch");
      const host = 'http://localhost:5000';
      const apiUrl = '/api/newuser'; 
      const data = {
        username: username,
        email: email,
        password: password
      };
      fetch(host + apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        mode: 'no-cors',
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        // Handle the response from the API here, e.g., show a success message or redirect the user to a different page
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle the error here, e.g., show an error message
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
.register-button {
  font: 500 1rem 'Quicksand', sans-serif;
}

.register-container{
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

.register-title {
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
  margin-left: auto;
  margin-right: auto;  
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

.form-input--error {
  color: var(--color-error);
  border-color: var(--color-error);
}

.form-input-error-message {
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: var(--color-error);
}

.register-button {
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

.register-button:hover {
  background: var(--color-primary-dark);
}

.register-button:active {
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