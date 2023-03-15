import { mount } from 'cypress/vue';
import Login from "../../src/components/Login.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Login />', () => {
  it('renders', () => {
    mount(Login);
  })
})