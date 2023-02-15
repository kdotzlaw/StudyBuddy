<template>
  <div class="container">
    <form class="form" id="login">
        <div class="login-container">
          <div class="form-input-group">
            <input type="text" id="signinUsername" class="form-input" autofocus placeholder="Username" v-model="username">
            <div class="form-input-error-message" v-if="usernameErrorMsg">{{ usernameErrorMsg }}</div>
          </div>
          <div class="form-input-group">
            <input type="password" id="signinPassword" class="form-input" autofocus placeholder="Password" v-model="password">
            <div class="form-input-error-message" v-if="passwordErrorMsg">{{ passwordErrorMsg }}</div>
          </div>
          <button class="login-button" type="button" @click="validateForm">Log In</button>
          <p class="form-text">
              <a href="#" class="form-link">Forgot your password?</a>
          </p>
          <p class="form-text">
              <a class="form-link" href="./" id="linkCreateAccount">Don't have an account? Create account</a>
          </p>
        </div>
    </form>
  </div>
</template>

<script setup>
  import{ ref } from "vue"
  import validate from "../logic/validate"

  const usernameErrorMsg = ref('');
  const passwordErrorMsg = ref('');

  function validateForm() {
    let username = document.getElementById("signinUsername").value;
    let password = document.getElementById("signinPassword").value;

    var userNameCheck = false;
    var passwordErrorCheck = true;

    console.log(username.length)

    if (validate.isInputEmpty(username)) {
      usernameErrorMsg.value = 'Username is required';
      userNameCheck = true;
    } else {
      usernameErrorMsg.value = '';
      userNameCheck = false;
    }

    if (validate.isInputEmpty(password)) {
      passwordErrorMsg.value = 'Password is required';
      passwordErrorCheck = true;
    } else {
      passwordErrorMsg.value = '';
      passwordErrorCheck = false;
    }

    if (!userNameCheck && !passwordErrorCheck) {
      const host = 'http://localhost:5000'; 
      const apiUrl = '/api/login';
      const data = {
        username: username,
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
      .then(response => console.log(response))
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

.form-input--error {
  color: var(--color-error);
  border-color: var(--color-error);
}

.form-input-error-message {
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: var(--color-error);
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