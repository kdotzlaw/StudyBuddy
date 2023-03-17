import { mount } from 'cypress/vue';
import Dashboard from "../../src/pages/Dashboard.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Dashboard />', () => {
  it('renders', () => {
    mount(Dashboard);
  })
})