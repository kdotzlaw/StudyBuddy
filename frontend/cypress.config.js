import { defineConfig } from "cypress";

export default defineConfig({
  projectId: "sbx6zb",
  videosFolder: "test/snapshots",
  screenshotsFolder: "test/snapshots",
  e2e: {
    "baseUrl": "http://localhost:5173",
    "env": {
      "serverUrl": "http://127.0.0.1:5000"
    },
    supportFile: "test/errorConfig.ts",
    specPattern: "test/acceptance/**/*.cy.{js,jsx,ts,tsx}",
  },
  component: {
    indexHtmlFile: "test/component/component-index.html",
    supportFile: false,
    video: false,
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },
});
