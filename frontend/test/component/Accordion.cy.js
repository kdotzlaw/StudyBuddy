import { mount } from 'cypress/vue';
import Accordion from "../../src/components/Accordion.vue";

describe('<Accordion />', () => {
  it('renders', () => {
    mount(Accordion);
  })
})