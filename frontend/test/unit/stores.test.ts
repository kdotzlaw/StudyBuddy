/*
 * stores.test.ts
 *    Tests on application-level Pinia store functions to ensure
 *    that they execute and update global store refs as expected.
 */

import { setActivePinia, createPinia, storeToRefs } from 'pinia';
import { useStore } from '../../src/stores';
import { describe, expect, test } from '@jest/globals';
import Timer from '../../src/logic/timer';

setActivePinia(createPinia());
const store = useStore();
const { 
    userId, pageName, 
    sessionTimer, studyTime, studyClass,
    isModalOpen, modalTitle, modalContent, modalRender,
    uiSkin, buddyChoice,
    reqSignal, gradeSignal
  } = storeToRefs(store);
const { 
    loginUser, logoutUser, setPageName,
    setTimer, setStudyTime, setStudyClass,
    toggleModal, setModal,
    updateSkin, updateBuddy,
    updateReqSignal, updateGradeSignal
  } = store;

let uID: String = "Ohlala a user";
describe('Test user login and logout', () => {

  test('Set userId from null (login)', () => {
    expect(userId.value).toBeNull();
    loginUser(uID);
    expect(userId.value).toBe(uID);
  })

  test('Set userId to null (logout)', () => {
    logoutUser();
    expect(userId.value).toBe(null);
  })

})

let cID: String = "classA";
let time: Number = 12;
describe('Test setting study timer, class, and time', () => {

  test('Change session timer (setTimer)', () => {
    setTimer(new Timer(uID, cID));
      expect(sessionTimer.value.getSessionUser()).toBe(uID);
      expect(sessionTimer.value.getCurrentClass()).toBe(cID);
      expect(sessionTimer.value.getTime()).toBeGreaterThanOrEqual(0);
  })

  test('Change active class (setStudyClass)', () => {
    setStudyClass(cID);
    expect(studyClass.value).toBe(cID);
  })

  test('Update study time (setStudyTime)', () => {
    setStudyTime(time);
    expect(studyTime.value).toBe(time);
  })

})

let page: String = "Page Name";
describe('Test current page name', () => {

  test('Set a page name (setPageName)', () => {
    setPageName(page);
    expect(pageName.value).toBe(page);
  })

})

let title: String = "The Amazing Wow";
let contentID: String = "much-amaze-wow";
let render: String = "<b> An HTML wow </b>";
describe('Test modal functions', () => {

  test('Switch modal state (toggleModal)', () => {
    toggleModal();
    expect(isModalOpen.value).toBeTruthy();
    toggleModal();
    expect(isModalOpen.value).not.toBeTruthy();
  })

  test('Set modal content (setModal)', () => {
    setModal(title, contentID, render);
    expect(modalTitle.value).toBe(title);
    expect(modalContent.value).toBe(contentID);
    expect(modalRender.value).toBe(render);
    expect(isModalOpen.value).toBeTruthy();
  })

})

let skin: String = "skin-forest";
let buddy: String = "Cat";
describe('Test user customizations', () => {

  test('Change UI skin (updateSkin)', () => {
    updateSkin(skin);
    expect(uiSkin.value).toBe(skin);
  })

  test('Change buddy choice (updateBuddy)', () => {
    updateBuddy(buddy);
    expect(buddyChoice.value).toBe(buddy);
  })

})

describe('Simulate dynamic update signals', () => {

  test('Emit requirements signal (updateReqSignal)', () => {
    updateReqSignal(true);
    expect(reqSignal.value).toBeTruthy();
    updateReqSignal(false);
    expect(reqSignal.value).not.toBeTruthy();
  })

  test('Emit grade signal (updateGradeSignal)', () => {
    updateGradeSignal(true);
    expect(gradeSignal.value).toBeTruthy();
    updateGradeSignal(false);
    expect(gradeSignal.value).not.toBeTruthy();
  })

})
