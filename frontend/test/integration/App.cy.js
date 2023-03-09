import { mount } from 'cypress/vue';
import { setActivePinia, createPinia } from 'pinia';
import App from "../../src/App.vue";

setActivePinia(createPinia());

describe('<App />', () => {
  it('renders', () => {
    mount(App);
  })
})