import { setActivePinia, createPinia, storeToRefs } from 'pinia';
import { useStore } from '../src/stores';
import { describe, expect, test } from '@jest/globals';

setActivePinia(createPinia());
const store = useStore();
const { userId, studyClass } = storeToRefs(store);
const { loginUser, logoutUser, setStudyClass } = store;

let userId1: String = "user1";
let userId2: String = "user2";
let class1: String = "classA";
let class2: String = "classB";

describe('Test user login from stores.js', () => {

  test('Set userId from null (login)', () => {
    expect(userId.value).toBeNull();
    loginUser(userId1);
    expect(userId.value).toBe(userId1);
  })
  test('Change active userId', () => {
      loginUser(userId2);
      expect(userId.value).toBe(userId2);
  })
  test('Set userId to null (logout)', () => {
      logoutUser();
      expect(userId.value).toBe(null);
  })

})

describe('Test setting study class from stores.js', () => {

  test('Set a class from null (login)', () => {
    expect(studyClass.value).toBeNull();
    setStudyClass(class1);
    expect(studyClass.value).toBe(class1);
  })
  test('Change active class', () => {
      setStudyClass(class2);
      expect(studyClass.value).toBe(class2);
  })

})