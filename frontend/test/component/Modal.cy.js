import { mount } from 'cypress/vue';
import Modal from "../../src/components/Modal.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Modal />', () => {
  it('renders', () => {
    mount(Modal);
  })
})