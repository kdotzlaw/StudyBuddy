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

  it('View important dates from Dashboard', () => {
    cy.wait(300)
  })

  it('View current and elapsed requirements from each class', () => {
    cy.wait(300)
  })

  it('Create new task', () => {
    cy.wait(300)
  })

  it('Edit a current task', () => {
    cy.wait(300)
  })

  it('Delete an existing task', () => {
    cy.wait(300)
  })

  it('Complete an existing task by assigning a grade', () => {
    cy.wait(300)
  })

  afterEach(() => {
    cy.wait(800)
  })
})