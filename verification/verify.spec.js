const { test, expect } = require('@playwright/test');

test('homepage has expected elements', async ({ page }) => {
  await page.goto('http://localhost:8000');

  // Wait for the page to be fully loaded
  await page.waitForLoadState('networkidle');

  // Scroll to the bottom of the page to ensure all elements are visible
  await page.evaluate(() => {
    window.scrollTo(0, document.body.scrollHeight);
  });

  // Take a screenshot of the entire page
  await page.screenshot({ path: '/home/jules/verification/verification.png', fullPage: true });
});
