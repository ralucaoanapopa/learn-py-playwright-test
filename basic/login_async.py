import asyncio, os
from playwright.async_api import Playwright, async_playwright, expect

base_URL = 'https://demoqa.com/'
login_URL = base_URL+'login'

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')

async def test_run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False, slow_mo=2000)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto(login_URL)
    await page.get_by_placeholder("UserName").click()
    await page.get_by_placeholder("UserName").fill(user_name)
    await page.get_by_placeholder("Password").click()
    await page.get_by_placeholder("Password").fill(user_pass)
    await page.get_by_role("button", name="Login").click()

    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await test_run(playwright)

asyncio.run(main())
