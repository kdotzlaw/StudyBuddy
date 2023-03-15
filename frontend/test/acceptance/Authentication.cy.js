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
      .type(randomUsername, { delay: 50 })
    cy.get('#signupEmail')
      .type(randomEmail, { delay: 50 })
    cy.get('#signupPassword')
      .type(randomPassword, { delay: 50 })
    cy.get('#signupPasswordConfirm')
      .type(randomPassword, { delay: 50 })
      .wait(300) 
    cy.request({
        method: "POST",
        url: `${serverUrl}/api/newuser`,
        headers: {
          'Content-Type': 'application/json',
        },
        mode: 'no-cors',
        credentials: 'include',
        body: JSON.stringify({
          username: randomUsername,
          email: randomEmail,
          password: randomPassword
        })
      }).should((response) => {
        expect(response.status).to.eq(200)
      })
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
      .type(randomUsername, { delay: 50 })
    cy.get('#signinPassword')
      .type(randomPassword, { delay: 50 })
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
      .type(randomUsername, { delay: 50 })
    cy.get('#signinPassword')
      .type(randomPassword, { delay: 50 })
    cy.get('.login-button').click()
      .wait(200)
    cy.get('.close').click()
      .wait(800)
    cy.get('#header-dropdown').trigger('mouseover')
      cy.contains('Log Out').click()
  })

  afterEach(() => {
    cy.wait(800)
  })
})


