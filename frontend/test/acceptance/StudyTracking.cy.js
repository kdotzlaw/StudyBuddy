/*
 * StudyTracking.cy.js
 *    Acceptance tests on timing and tracking study sessions user stories.
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
      .wait(5000)
  })

  it('Update study sessions and study time from Dashboard', () => {
    cy.get('#classCards')
      .find('.play-btn')
      .each(($button) => {
        cy.wrap($button).click()
          .wait(2200)
        cy.get('#timerExpress div').should('have.text', '00:02')
      })
  })

  it('Update study sessions and study time from existing Class pages', () => {
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('.round').click()
      .wait(2200)
      .click()
    cy.get('#timerExpress div').should('have.text', '00:02')
  })

  afterEach(() => {
    cy.wait(800)
  })
})