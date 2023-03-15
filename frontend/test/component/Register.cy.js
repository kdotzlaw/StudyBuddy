import { mount } from 'cypress/vue';
import Register from "../../src/components/Register.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Register />', () => {
  it('renders', () => {
    mount(Register);
  })
})