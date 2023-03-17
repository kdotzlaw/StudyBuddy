import { mount } from 'cypress/vue';
import router from '../../src/router';
import CreateClass from "../../src/pages/CreateClass.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<CreateClass />', () => {
  it('renders', () => {
    // Setup options object
    let options = {};
    options.global = options.global || {};
    options.global.plugins = options.global.plugins || [];

    cy.wrap(router.push('/editClass/mock'));

    // Add router plugin
    options.global.plugins.push({
      install(app) {
        app.use(router)
      },
    });

    mount(CreateClass, options);
  })
})