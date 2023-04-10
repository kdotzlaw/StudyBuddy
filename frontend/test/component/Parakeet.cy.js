import { mount } from 'cypress/vue';
import Parakeet from "../../src/components/Parakeet.vue";

describe('<Parakeet />', () => {
  it('renders', () => {
    mount(Parakeet);
  })
})