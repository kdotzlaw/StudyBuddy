import { mount } from 'cypress/vue';
import router from '../../src/router';
import GradeCalculator from "../../src/pages/GradeCalculator.vue";
import { setActivePinia, createPinia } from 'pinia';
setActivePinia(createPinia());

describe('<GradeCalculator />', () => {
  it('renders', () => {
    // Setup options object
    let options = {};
    options.global = options.global || {};
    options.global.plugins = options.global.plugins || [];

    cy.wrap(router.push('/gradeCalculator/mock'));

    // Add router plugin
    options.global.plugins.push({
      install(app) {
        app.use(router)
      },
    });

    mount(GradeCalculator, options);
  })
})