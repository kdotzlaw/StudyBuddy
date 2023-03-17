import { mount } from 'cypress/vue';
import Header from "../../src/components/Header.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Header />', () => {
  it('renders', () => {
    mount(Header);
  })
})