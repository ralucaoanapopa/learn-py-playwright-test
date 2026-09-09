import os
from playwright.async_api import async_playwright
import pytest

base_URL = 'https://demoqa.com/'
login_URL = base_URL+'login'

user_name = os.environ.get('USERNAME_QA')
user_pass = os.environ.get('PASSWORD_QA')


@pytest.mark.asyncio
async def test_run() -> None:
    async with async_playwright() as playwright:
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
