/*
 * filter.test.ts
 *    Tests on form input validation functions to identify empty fields
 *    and enforce security checks.
 */

import {describe, expect, test} from '@jest/globals';
import filter from '../../src/logic/filter';
import type {reqsEntry, chatsEntry} from '../../src/logic/filter';

let assignment1: reqsEntry = {
  classKey: "COMP4620", 
  tagColor: "red", 
  name: "Assignment 1", 
  due: new Date("January 1, 2023"), 
  goal: "C"
};
let assignment2: reqsEntry = {
  classKey: "COMP4620", 
  tagColor: "red", 
  name: "Assignment 2", 
  due: new Date("January 28, 2023"), 
  goal: "C"
};
let assignment3: reqsEntry = {
  classKey: "COMP3030", 
  tagColor: "green", 
  name: "Assignment 3", 
  due: new Date("February 6, 2023"), 
  goal: "A+"
};
let assignment4: reqsEntry = {
  classKey: "COMP3030", 
  tagColor: "green", 
  name: "Assignment 4", 
  due: new Date("March 18, 2023"), 
  goal: "A+"
};
let assignment5: reqsEntry = {
  classKey: "COMP1010", 
  tagColor: "blue", 
  name: "Final", 
  due: new Date("April 10, 2023"), 
  goal: "F"
};
let assignment6: reqsEntry = {
  classKey: "COMP1020", 
  tagColor: "purple", 
  name: "Mid Term", 
  due: new Date("March 1, 2023"), 
  goal: "D-"
};
let assignmentList1: reqsEntry[] = [assignment1, assignment2, assignment3, assignment4, assignment5];
let assignmentList2: reqsEntry[] = [assignment5, assignment2, assignment4, assignment3, assignment1];
let assignmentList3: reqsEntry[] = [assignment2, assignment3, assignment4, assignment5, assignment6];
let assignmentList4: reqsEntry[] = [assignment1, assignment2, assignment3, assignment4, assignment5, assignment6];
let assignmentList5: reqsEntry[] = [assignment1, assignment2, assignment3];
let assignmentList6: reqsEntry[] = [assignment1, assignment3];


describe('Test Assignment Ordering', () => {
  test('Input in Correct Order', () => {
    expect(filter.getReqs(assignmentList1)).toEqual(assignmentList1);
  })

  test('Input in Incorrect Order', () => {
    expect(filter.getReqs(assignmentList2)).toEqual(assignmentList1);
  })

  test('Test for Incorrect Output', () => {
    expect(filter.getReqs(assignmentList1)).not.toEqual(assignmentList3);
  })

  test('Test for Correct Subset', () => {
    expect(filter.getReqs(assignmentList1)).not.toEqual(assignmentList5);
  })

  test('Test for Incorrect Subset', () => {
    expect(filter.getReqs(assignmentList3)).not.toEqual(assignmentList5);
  })
})

describe('Test Assignment Output Length', () => {
  test('Input of 0 assignments', () => {
    expect(filter.getReqs([]).length).toBe(0);
  })

  test('Input of 3 assignments', () => {
    expect(filter.getReqs(assignmentList5).length).toBe(3);
  })

  test('Input of 5 assignments', () => {
    expect(filter.getReqs(assignmentList1).length).toBe(5);
  })

  test('Input of 6 assignments', () => {
    expect(filter.getReqs(assignmentList4).length).toBe(5);
  })
})

describe('Test Chat Output', () => {
  test('No Deadlines', () => {
    expect(filter.getChats([])).toEqual(
      expect.arrayContaining(["You have no upcoming deadlines."]));
  })

  test('Vowel Grade', () => {
    expect(filter.getChats([assignment3])).toEqual(
      expect.arrayContaining(["Don't forget! You're aiming for an A+ for your class: COMP3030!"]));
  })

  test('Not Vowel Grade', () => {
    expect(filter.getChats([assignment3])).not.toEqual(
      expect.arrayContaining(["Don't forget! You're aiming for a A+ for your class: COMP3030!"]));
  })

  test('Consonant Grade', () => {
    expect(filter.getChats([assignment1])).toEqual(
      expect.arrayContaining(["Don't forget! You're aiming for a C for your class: COMP4620!"]));
  })

  test('Not Consonant Grade', () => {
    expect(filter.getChats([assignment3])).not.toEqual(
      expect.arrayContaining(["Don't forget! You're aiming for an C for your class: COMP4620!"]));
  })

  let expected = [
    "You have an upcoming deadline, \"Assignment 1\" for your class: COMP4620. It is due on January 1!",
    "You have an upcoming deadline, \"Assignment 2\" for your class: COMP4620. It is due on January 28!",
    "You have an upcoming deadline, \"Assignment 3\" for your class: COMP3030. It is due on February 6!",
    "You have an upcoming deadline, \"Assignment 4\" for your class: COMP3030. It is due on March 18!",
    "You have an upcoming deadline, \"Final\" for your class: COMP1010. It is due on April 10!",
  ]
  test('All Deadlines Included', () => {
    expect(filter.getChats(assignmentList1)).toEqual(
      expect.arrayContaining(expected));
  })
})

