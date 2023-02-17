import {describe, expect, test} from '@jest/globals';
import validate from '../src/logic/validate';

let userId1: String = "";
let userId2: String = "user2";
let password1: String = "";
let password2: String = "password";

describe('Validate String Cases', () => {

  test('Testing if string is infact empty', () => {
    
    expect(validate.isInputEmpty(userId1)).toBe(true);
  })

  test('Testing if string is not empty', () => {
    
    expect(validate.isInputEmpty(userId2)).toBe(false);
  })

})

describe('Validate Password Test Case', () => {

  test('Testing password is equal or greater than 8 characters', () => {
    
    expect(validate.isValidPassword(password1)).toBe(true);
  })

  test('Testing password is less than 8 characters', () => {
    
    expect(validate.isValidPassword(password2)).toBe(false);
  })

})