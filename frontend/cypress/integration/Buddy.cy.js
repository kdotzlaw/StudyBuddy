import Buddy from "../../src/components/Buddy.vue";

describe('<Buddy />', () => {
  it('renders', () => {
    cy.mount(Buddy);
  })
})