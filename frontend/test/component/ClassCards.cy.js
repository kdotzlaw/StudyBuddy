import { mount } from 'cypress/vue';
import ClassCards from "../../src/components/ClassCards.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<ClassCards />', () => {
  it('renders', () => {
    mount(ClassCards);
  })
})