/*
 * timer.test.ts
 *    Tests on Timer class initialization, functions, and management.
 */

import {describe, expect, test} from '@jest/globals';
import Timer from '../src/logic/timer';

let timer: Timer;
let userId1: String = "user1";
let userId2: String = "user2";
let class1: String = "classA";
let class2: String = "classB";

describe('Construct Timer and test values', () => {

  test('Constructing Timer class', () => {
    timer = new Timer(userId1,class1); 
    expect(timer).not.toBeNull();
  })

  test('Testing session user value', () => {
    timer = new Timer(userId1,class1); 
    expect(timer.getSessionUser()).toEqual(userId1);
  })

  test('Testing current class value', () => {
    timer = new Timer(userId1,class1); 
    expect(timer.getCurrentClass()).toEqual(class1);
  })

})


describe('Test timer functions', () => {
  
  test('Testing getTime function', () => {
    timer = new Timer(userId1,class1); 
    expect(timer.getTime()).toBeGreaterThanOrEqual(0);
  })

  test('Testing isPaused function', () => {
    timer = new Timer(userId1,class1); 
    expect(timer.isPaused()).toEqual(false);
  })

  test('Testing pause function', () => {
    timer = new Timer(userId1,class1); 
    timer.pause();
    expect(timer.isPaused()).toEqual(true);
  })

  test('Testing resume function', () => {
    timer = new Timer(userId1,class1); 
    timer.pause();
    timer.resume();
    expect(timer.isPaused()).toEqual(false);
  })

})