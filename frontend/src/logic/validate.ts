
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