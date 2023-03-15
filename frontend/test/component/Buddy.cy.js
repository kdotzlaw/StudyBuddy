import { mount } from 'cypress/vue';
import Buddy from "../../src/components/Buddy.vue";

describe('<Buddy />', () => {
  it('renders', () => {
    mount(Buddy);
  })
})