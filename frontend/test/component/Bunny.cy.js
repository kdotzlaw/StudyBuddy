import { mount } from 'cypress/vue';
import Bunny from "../../src/components/Bunny.vue";

describe('<Bunny />', () => {
  it('renders', () => {
    mount(Bunny);
  })
})