import { defineConfig } from "cypress";

export default defineConfig({
  projectId: "sbx6zb",
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },

  component: {
    video: false,
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },
});
