import { mount } from 'cypress/vue';
import ModalManager from "../../src/components/ModalManager.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<ModalManager />', () => {
  it('renders', () => {
    mount(ModalManager);
  })
})