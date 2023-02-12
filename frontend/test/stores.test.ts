import { setActivePinia, createPinia, storeToRefs } from 'pinia';
import { useStore } from '../src/stores';
import { describe, expect, it } from '@jest/globals';

setActivePinia(createPinia());
const store = useStore();
const { userId } = storeToRefs(store);
const { loginUser, logoutUser } = store;

let userId1: String = "user1";
let userId2: String = "user2";

describe('Test user login from stores.js', () => {

    it('Set userId from null (login)', () => {
      expect(userId.value).toBeNull();
      loginUser(userId1);
      expect(userId.value).toBe(userId1);
    })
  
    it('Change active userId', () => {
        loginUser(userId2);
        expect(userId.value).toBe(userId2);
    })

    it('Set userId to null (logout)', () => {
        logoutUser();
        expect(userId.value).toBe(null);
    })
  })