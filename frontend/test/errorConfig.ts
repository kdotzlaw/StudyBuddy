/*
 * e2e.ts
 *    Support file to nullify application errors during remote acceptance testing.
 */

/// <reference types="cypress" />

Cypress.on('uncaught:exception', (err, runnable) => {
    return false
})