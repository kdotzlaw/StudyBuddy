/*
 * Authentication.cy.js
 *    Acceptance tests on account creation, login, and logout user stories.
 */

/// <reference types="cypress" />

const serverUrl = Cypress.env('serverUrl');
let randomUsername = Math.random().toString(36).substring(2, 10);
let randomEmail = randomUsername + "@email.com";
let randomPassword = Math.random().toString(36).substring(2, 10);

context('Actions', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('Create a new account', () => {
    cy.wait(300)
    cy.get('#header-dropdown').trigger('mouseover')
      .wait(300)
    cy.contains('Login').click()
      .wait(500)
    cy.get('#linkCreateAccount').click()
      .wait(300)
    cy.get('#signupUsername')
      .type(randomUsername, { delay: 20 })
    cy.get('#signupEmail')
      .type(randomEmail, { delay: 20 })
    cy.get('#signupPassword')
      .type(randomPassword, { delay: 20 })
    cy.get('#signupPasswordConfirm')
      .type(randomPassword, { delay: 20 })
      .wait(300) 
    cy.get('.register-button').click()
      .wait(800)
    cy.get('.close').click()
  })

  it('Login existing user', () => {
    cy.wait(300)
    cy.get('#header-dropdown').trigger('mouseover')
      .wait(300)
    cy.contains('Login').click()
      .wait(500)
    cy.get('#signinUsername')
      .type(randomUsername, { delay: 20 })
    cy.get('#signinPassword')
      .type(randomPassword, { delay: 20 })
      .wait(300)
    cy.get('.login-button').click()
      .wait(800)
    cy.get('.close').click()
  })

  it('Logout existing user', () => {
    cy.get('#header-dropdown').trigger('mouseover')
    cy.contains('Login').click()
      .wait(500)
    cy.get('#signinUsername')
      .type(randomUsername, { delay: 20 })
    cy.get('#signinPassword')
      .type(randomPassword, { delay: 20 })
    cy.get('.login-button').click()
      .wait(200)
    cy.get('.close').click()
      .wait(800)
    cy.get('#header-dropdown', { timeout: 20000 }).trigger('mouseover')
      cy.contains('Log Out').click()
  })

  afterEach(() => {
    cy.wait(800)
  })
})