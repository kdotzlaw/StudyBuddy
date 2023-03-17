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
      .wait(300)
  })

  it('View estimated letter grades from all classes', () => {
    cy.get('#workspace')
      .scrollTo('bottom')
    cy.get('#classCards')
      .find('.play-btn')
      .each(($button) => {
        cy.wrap($button).click()
          .wait(2200)
        cy.get('#timerExpress div').should('have.text', '00:02')
      })
  })

  it('Completed requirements from each class should have a letter grade assigned', () => {
    cy.wait(300)
  })

  it('Create grading scheme', () => {
    cy.wait(300)
  })

  it('Update grading scheme', () => {
    cy.wait(300)
  })

  afterEach(() => {
    cy.wait(800)
  })
})