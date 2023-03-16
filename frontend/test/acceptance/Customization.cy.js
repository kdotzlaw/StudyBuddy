/* 
 * Note: Customization has been decoupled from Progression (labelled as Future Sprint outside project scope) 
 * due to time constraints on the project. This spec will only address customization user stories.
 */

/// <reference types="cypress" />

const serverUrl = Cypress.env('serverUrl');

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

  it('Check for tailored Buddy Feed based on user study progress', () => {
    cy.wait(300)
  })

  it('Check for tailored Buddy Feed based on approaching deadlines', () => {
    cy.wait(300)
  })

  it('Customize UI with unlockables', () => {
    cy.wait(300)
  })

  it('Customize companion with unlockables', () => {
    cy.wait(300)
  })

  afterEach(() => {
    cy.wait(800)
  })
})