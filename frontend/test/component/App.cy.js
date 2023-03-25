import App from "../../src/App.vue";
import { mount } from 'cypress/vue';
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<App />', () => {
  it('renders', () => {
    mount(App);
  })
})