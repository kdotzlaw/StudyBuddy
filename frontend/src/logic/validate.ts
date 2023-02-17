/*
 * validate.ts
 *    Form input validation functions to identify empty fields and enforce security checks.
 */


function isInputEmpty(input: String): boolean{
  return input.length == 0;
}

function isValidPassword(input: String): boolean{
  return input.length < 8;
}

export default{
  isInputEmpty,
  isValidPassword
}