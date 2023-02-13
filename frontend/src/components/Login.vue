<template>
  <div class="container">
    <form class="form" id="login">
        <h1 class="form-title">Login</h1>
        <div class="login-container">
          <div class="form-input-group">
            <input type="text" id="signinUsername" class="form-input" autofocus placeholder="Username" v-model="username">
            <div class="form-input-error-message" v-if="usernameError">{{ usernameError }}</div>
          </div>
          <div class="form-input-group">
            <input type="password" class="form-input" autofocus placeholder="Password" v-model="password">
            <div class="form-input-error-message" v-if="passwordError">{{ passwordError }}</div>
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

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      usernameError: '',
      passwordError: '',
    };
  },
  methods: {
    validateForm() {

      if (!this.username) {
        this.usernameError = 'Username is required';
      } else {
        this.usernameError = '';
      }

      if (!this.password) {
        this.passwordError = 'Password is required';
      } else {
        this.passwordError = '';
      }

      if (!this.usernameErrorr && !this.passwordError) {
        const apiUrl = '127.0.0.1:5000/api'; 
        const data = {
          username: this.username,
          password: this.password
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
  }
};
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