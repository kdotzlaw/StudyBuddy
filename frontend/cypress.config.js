import { defineConfig } from "cypress";

export default defineConfig({
  projectId: "sbx6zb",
  videosFolder: "test/snapshots",
  screenshotsFolder: "test/snapshots",
  e2e: {
    supportFile: false,
    specPattern: "test/acceptance/**/*.cy.{js,jsx,ts,tsx}",
  },
  component: {
    indexHtmlFile: "test/integration/component-index.html",
    supportFile: false,
    video: false,
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },
});
