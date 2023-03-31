/*
 * ClassManagement.cy.js
 *    Acceptance tests on class workspace creation and management user stories.
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
      .wait(300)
    cy.get('#workspace')
      .scrollTo('bottom')
  })

  it('Create a new class', () => {
    cy.get('.addNew', { timeout: 20000 }).click()
      .wait(200)
    cy.get('.pageNameSection').should('have.text', 'Create New Class')
    cy.get('#class-name-input')
      .type("Software Engineering 2", { delay: 20 })
    cy.get('#class-time-input')
      .type("11:30-12:15 TR", { delay: 20 })
    cy.get('#class-code-input')
      .type(courseCode, { delay: 20 })
    cy.get('.bar').click()
  })

  it('Check new class workspace has been created from Dashboard', () => {
    cy.contains(courseCode, { timeout: 20000 }).click()
  })

  it('Update class information', () => {
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('#class-settings').trigger('mouseover')
      .wait(300)
      .click()
      .wait(200)
    cy.get('.pageNameSection').should('have.text', 'Manage Class')
    cy.get('#class-name-input')
      .type("Software Engineering 2", { delay: 20 })
    cy.get('#class-time-input')
      .type("11:30-12:15 TR", { delay: 20 })
    cy.get('#class-code-input')
      .type(courseCode, { delay: 20 })
    cy.get('#professor-name-input')
      .type("Dr. Badoogie Doogie", { delay: 20 })
    cy.get('#professor-email-input')
      .type("badoogie@email.com", { delay: 20 })
    cy.get('#professor-office-input')
      .type("700 Machray", { delay: 20 })
    cy.get('.bar').click()
  })

  afterEach(() => {
    cy.wait(800)
  })
})