import { mount } from 'cypress/vue';
import Corgi from "../../src/components/Corgi.vue";

describe('<Corgi />', () => {
  it('renders', () => {
    mount(Corgi);
  })
})