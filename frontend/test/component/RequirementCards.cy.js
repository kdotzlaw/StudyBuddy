import { mount } from 'cypress/vue';
import RequirementCards from "../../src/components/RequirementCards.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<RequirementCards />', () => {
  it('renders', () => {
    mount(RequirementCards);
  })
})