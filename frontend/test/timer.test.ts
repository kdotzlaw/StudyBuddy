import {describe, expect, test} from '@jest/globals';
import Timer from '../src/logic/timer';

let timer: Timer;
let userId1: String = "user1";
let userId2: String = "user2";
let class1: String = "classA";
let class2: String = "classB";

describe('Construct Timer', () => {
  test('Constructing Timer class', () => {
    timer = new Timer(userId1,class1); 
    expect(timer).not.toBeNull();
  });
});