import asyncio
from playwright.async_api import async_playwright, expect

from page_titles import PageTitles

base_url = "https://playwright.dev/"


async def use_chromium(playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=200)
    page = await browser.new_page()
    await page.goto(base_url)
    await expect(page).to_have_title(PageTitles.PLAYWRIGHT)
    await browser.close()


async def use_firefox(playwright):
    browser = await playwright.firefox.launch(headless=False, slow_mo=200)
    page = await browser.new_page()
    await page.goto(base_url)
    await expect(page).to_have_title(PageTitles.PLAYWRIGHT)
    await browser.close()


async def use_webkit(playwright):
    browser = await playwright.webkit.launch(headless=False, slow_mo=200)
    page = await browser.new_page()
    await page.goto(base_url)
    await expect(page).to_have_title(PageTitles.PLAYWRIGHT)
    await browser.close()


async def main():
    async with async_playwright() as p:
        await use_chromium(p)
        await use_firefox(p)
        await use_webkit(p)

asyncio.run(main())
