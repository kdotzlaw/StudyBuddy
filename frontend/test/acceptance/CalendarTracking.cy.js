/*
 * CalendarTracking.cy.js
 *    Acceptance tests on calendar task views and CRUD user stories.
 */

/// <reference types="cypress" />

const serverUrl = Cypress.env('serverUrl');

let courseCode = "COMP 4350";

context('Actions', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.get('#header-dropdown').trigger('mouseover')
    cy.contains('Login').click()
      .wait(500)
    cy.get('#signinUsername')
      .type("andrea22", { delay: 20 })
    cy.get('#signinPassword')
      .type("2222", { delay: 20 })
    cy.get('.login-button').click()
      .wait(200)
    cy.get('.close').click()
      .wait(800)
  })

  it('View important dates from Dashboard', () => {
    cy.contains('Calendar Overview').click()
      .wait(20000)
    cy.get('#reqCards')
      .find('.dues')
      .each(($date) => {
        cy.wrap($date).should('not.be.empty')
      })
    cy.get('#workspace')
      .scrollTo('bottom')
      .wait(200)
      .scrollTo('top')
    cy.contains('Calendar Overview').click()
  })

  it('View current and elapsed requirements from each class', () => {
    cy.get('#workspace')
      .scrollTo('bottom')
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('#reqCards').should('exist')
    cy.get('#change-view').click()
      .wait(100)
    cy.get('#reqCards').should('exist')
  })

  it('Create new task', () => {
    cy.get('#workspace')
      .scrollTo('bottom')
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.contains('Add Requirements').click()
      .wait(200)
    cy.get('#name-req-input').type('Assignment 1')
    cy.get('#date-req-input').type('2023-03-28T09:00')
    cy.get('#grade-req-input').type('A')
    cy.get('#add-button').click()
  })

  it('Edit a current task', () => {
    cy.get('#workspace')
      .scrollTo('bottom')
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('.reqManage').first().click()
      .wait(200)
    cy.get('#name-req-input').type('New Task Name')
    cy.get('#date-req-input').type('2023-03-28T09:00')
    cy.get('#grade-req-input').type('A')
    cy.get('#add-button').click()
  })

  it('Delete an existing task', () => {
    cy.get('#workspace')
      .scrollTo('bottom')
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('.reqManage').first().click()
      .wait(200)
    cy.get('#delete-button').click()
  })

  it('Complete an existing task by assigning a grade', () => {
    cy.get('#workspace')
      .scrollTo('bottom')
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('.reqManage').first().click()
      .wait(200)
    cy.get('#name-req-input').type('New Task Name')
    cy.get('#date-req-input').type('2023-03-28T09:00')
    cy.get('#grade-req-input').type('A')
    cy.get('#finish-req-input').type('A')
    cy.get('#add-button').click()
  })

  afterEach(() => {
    cy.wait(800)
  })
})