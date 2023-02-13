<template>
  <div>
    <form class="form " id="createAccount">
      <h1 class="register-title">Create Account</h1>
      <!-- <div class="form-message form-message--error"></div> -->
      <div class="register-container">
        <div class="form-input-group">
          <input type="text" id="signupUsername" class="form-input" autofocus placeholder="Username" v-model="username">
          <div class="form-input-error-message" v-if="usernameErrorMsg">{{ usernameErrorMsg }}</div>
        </div>
        <div class="form-input-group">
            <input type="text" id="email" class="form-input" autofocus placeholder="Email Address" v-model="email">
            <div class="form-input-error-message" v-if="emailErrorMsg">{{ emailErrorMsg }}</div>
        </div>
        <div class="form-input-group">
            <input type="password" id = "password" class="form-input" autofocus placeholder="Password" v-model="password">
            <div class="form-input-error-message" v-if="passwordErrorMsg">{{ passwordErrorMsg }}</div>
        </div>
        <div class="form-input-group">
            <input type="password" id = "passwordConfirm" class="form-input" autofocus placeholder="Confirm password" v-model="confirmPassword">
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

  const usernameErrorMsg = ref('');
  const emailErrorMsg = ref('');
  const passwordErrorMsg = ref('');
  const confirmpasswordErrorMsg = ref('');

  function validateForm() {
    let username = document.getElementById("signupUsername").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("passwordConfirm").value;

    var userNameCheck = false;
    var emailCheck = false;
    var passwordErrorCheck = false;
    var passwordConfirmErrorCheck = false;
    var passwordLengthCheck = false;

    if (username.length == 0) {
      usernameErrorMsg.value = 'Username is required';
      userNameCheck = true;
    } else {
      usernameErrorMsg.value = '';
      userNameCheck = false;
    }

    if (email.length == 0) {
      emailErrorMsg.value = 'Email is required';
      emailCheck = true;
    } else {
      emailErrorMsg.value = '';
      emailCheck = false;
    }

    if (password.length == 0) {
      passwordErrorMsg.value = 'Password is required';
    } else if(password.length < 8){
      passwordErrorMsg.value = 'Password length must be more than 8 or more characters';
      passwordErrorCheck = true;
    } else {
      passwordErrorMsg.value = '';
      passwordErrorCheck = false;
    }

    if (confirmPassword.length == 0) {
      confirmpasswordErrorMsg.value = 'Confirm password is required';
      passwordConfirmErrorCheck = true;
    } else {
      confirmpasswordErrorMsg.value = '';
      passwordConfirmErrorCheck = false;
    }

    if(!passwordErrorMsgCheck && !(password == confirmPassword) && confirmPassword.length > 0){
      passwordErrorMsg.value = 'Password does not match';
      confirmpasswordErrorMsg.value = 'Password does not match';
      passwordLengthCheck = true;
    } else{
      passwordLengthCheck = false;
    }
    

    if (!userNameCheck && !emailCheck && !passwordErrorCheck && !passwordConfirmErrorCheck && !passwordLengthCheck) {
      const apiUrl = '/api/login'; 
      const data = {
        username: username,
        email: email,
        password: password
      };
      fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
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