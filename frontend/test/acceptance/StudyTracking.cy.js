/// <reference types="cypress" />

const serverUrl = Cypress.env('serverUrl');

context('Actions', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.get('#header-dropdown').trigger('mouseover')
    cy.contains('Login').click()
      .wait(500)
    cy.get('#signinUsername')
      .type("andrea22", { delay: 50 })
    cy.get('#signinPassword')
      .type("2222", { delay: 50 })
    cy.get('.login-button').click()
      .wait(200)
    cy.get('.close').click()
      .wait(800)
  })

  it('Update study sessions and study time from Dashboard', () => {
    cy.wait(300)
  })

  it('Update study sessions and study time from existing Class pages', () => {
    cy.wait(300)
  })

  afterEach(() => {
    cy.wait(800)
  })
})

