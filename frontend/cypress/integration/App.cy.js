import { setActivePinia, createPinia } from 'pinia';
import App from "../../src/App.vue";

setActivePinia(createPinia());

describe('<App />', () => {
  it('renders', () => {
    cy.mount(App);
  })
})