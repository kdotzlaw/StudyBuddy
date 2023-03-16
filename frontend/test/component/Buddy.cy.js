import { mount } from 'cypress/vue';
import Buddy from "../../src/components/Buddy.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Buddy />', () => {
  it('renders', () => {
    mount(Buddy);
  })
})