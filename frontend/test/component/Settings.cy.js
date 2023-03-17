import { mount } from 'cypress/vue';
import Settings from "../../src/components/Settings.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Settings />', () => {
  it('renders', () => {
    mount(Settings);
  })
})