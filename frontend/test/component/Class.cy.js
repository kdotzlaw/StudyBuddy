import { mount } from 'cypress/vue';
import router from '../../src/router';
import Class from "../../src/pages/Class.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<Class />', () => {
  it('renders', () => {
    // Setup options object
    let options = {};
    options.global = options.global || {};
    options.global.plugins = options.global.plugins || [];

    cy.wrap(router.push('/class/mock'));

    // Add router plugin
    options.global.plugins.push({
      install(app) {
        app.use(router)
      },
    });

    mount(Class, options);
  })
})