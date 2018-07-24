const puppeteer = require('puppeteer');

async function clickButton(url) {

  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);
  await page.screenshot({path: 'google.png'});

  await browser.close();
}

var image = getPic();
