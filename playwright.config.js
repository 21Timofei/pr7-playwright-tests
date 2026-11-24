const { defineConfig } = require('@playwright/test');
const path = require('node:path');

// Браузер хранится внутри проекта, чтобы не менять системное окружение.
process.env.PLAYWRIGHT_BROWSERS_PATH ||= path.join(__dirname, '.browsers');

module.exports = defineConfig({
  testDir: './tests',
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    browserName: 'chromium',
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
  },
});
