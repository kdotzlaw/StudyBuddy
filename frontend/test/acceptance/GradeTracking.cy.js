/*
 * GradeTracking.cy.js
 *    Acceptance tests on grade tracking user stories.
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

  it('View estimated letter grades from all classes', () => {
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('#grade', { timeout: 20000 }).should('not.be.empty')
      .wait(200)
  })

  it('Completed requirements from each class should have a letter grade assigned', () => {
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.get('#change-view').click()
      .wait(100)
    cy.get('.goal', { timeout: 20000 }).each(($grade) => {
      cy.wrap($grade).should('not.equal','')
    })
  })

  it('Create grading scheme', () => {
    cy.contains(courseCode, { timeout: 20000 }).click()
      .wait(200)
    cy.contains('Grade breakdown').click()
      .wait(200)
    
    // Add two new breakdown fields
      cy.get('#add-row').click()
    cy.get('#add-row').click()
      .wait(50)
    
    // Fill up fields
    cy.get('#table-buddy tr:nth-child(1) td:nth-child(1)').type("Quiz", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(1) td:nth-child(2)').type("4", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(1) td:nth-child(3)').type("20", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(2) td:nth-child(1)').type("Assignment", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(2) td:nth-child(2)').type("2", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(2) td:nth-child(3)').type("30", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(3) td:nth-child(1)').type("Final Exam", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(3) td:nth-child(2)').type("1", { delay: 20 })
    cy.get('#table-buddy tr:nth-child(3) td:nth-child(3)').type("50", { delay: 20 })

    // Submit
    cy.get('#save-button button').click()
  })

  afterEach(() => {
    cy.wait(800)
  })
})