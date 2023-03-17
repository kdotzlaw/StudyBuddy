/*
 * Customization.cy.js
 *    Acceptance tests on dashboard feed and customization user stories.
 *    Note: Customization has been decoupled from Progression (labelled as Future Sprint outside project scope)
 */

/// <reference types="cypress" />

const serverUrl = Cypress.env('serverUrl');

context('Actions', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.get('#header-dropdown').trigger('mouseover')
  })

  it('Check for tailored Buddy Feed based on user study progress', () => {
    cy.contains('Login').click()
      .wait(200)
    cy.get('#signinUsername')
      .type("andrea22", { delay: 20 })
    cy.get('#signinPassword')
      .type("2222", { delay: 20 })
    cy.get('.login-button').click()
      .wait(200)
    cy.get('.close').click()
    cy.get('#chat-balloon p', { timeout: 14000 })
      .should('include.text', 'start studying')
  })

  it('Check for tailored Buddy Feed based on approaching deadlines', () => {
    cy.contains('Login').click()
      .wait(200)
    cy.get('#signinUsername')
      .type("andrea22", { delay: 20 })
    cy.get('#signinPassword')
      .type("2222", { delay: 20 })
    cy.get('.login-button').click()
      .wait(200)
    cy.get('.close').click()
    cy.get('#chat-balloon p', { timeout: 14000 })
      .should('include.text', 'upcoming deadline')
  })

  it('Customize UI with unlockables', () => {
    cy.contains('Manage Settings').click()
      .wait(200)
    cy.get('.skins')
      .find('.skin-preview')
      .each(($div) => {
        cy.wrap($div).click()
          .wait(300)
      })
    cy.get('.close').click()
  })

  it('Customize companion with unlockables', () => {
    cy.contains('Manage Settings').click()
      .wait(200)
    cy.get('.buddies')
      .find('.buddy-preview')
      .each(($div) => {
        cy.wrap($div).click()
          .wait(300)
      })
    cy.get('.close').click()
  })

  afterEach(() => {
    cy.wait(800)
  })
})