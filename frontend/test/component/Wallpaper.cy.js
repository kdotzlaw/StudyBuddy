import { mount } from 'cypress/vue';
import Wallpaper from "../../src/components/Wallpaper.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Wallpaper />', () => {
  it('renders', () => {
    mount(Wallpaper);
  })
})