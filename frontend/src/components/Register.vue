<template>
  <div>
    <form class="form " id="createAccount">
      <h1 class="register-title">Create Account</h1>
      <!-- <div class="form-message form-message--error"></div> -->
      <div class="register-container">
        <div class="form-input-group">
          <input type="text" id="signupUsername" class="form-input" autofocus placeholder="Username">
          <div class="form-input-error-message"></div>
        </div>
        <div class="form-input-group">
            <input type="text" class="form-input" autofocus placeholder="Email Address">
            <div class="form-input-error-message"></div>
        </div>
        <div class="form-input-group">
            <input type="password" class="form-input" autofocus placeholder="Password">
            <div class="form-input-error-message"></div>
        </div>
        <div class="form-input-group">
            <input type="password" class="form-input" autofocus placeholder="Confirm password">
            <div class="form-input-error-message"></div>
        </div>
        <button class="register-button" type="submit">Register</button>
        <p class="form-text">
            <a class="form-link" href="./" id="linkLogin">Already have an account? Sign in</a>
        </p>
      </div>
    </form>
  </div>
</template>

<script>

export default {
  
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

.register-buttonn:hover {
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