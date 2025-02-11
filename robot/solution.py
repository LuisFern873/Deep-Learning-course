import asyncio
import time
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright) -> None:

    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(ignore_https_errors=True)
    page = await context.new_page()
    await page.goto("https://192.168.1.1")
    await page.locator("#mainFrame").content_frame.get_by_role("textbox").click()
    await page.locator("#mainFrame").content_frame.get_by_role("textbox").fill("#330844@ED00F7*")
    await page.locator("#mainFrame").content_frame.get_by_role("button", name="Entrar").click()
    click_task = page.locator("#mainFrame").content_frame.get_by_role("cell", name="MENU").click()
    hover_task = page.locator("#mainFrame").content_frame.get_by_role("cell", name="MENU").hover()
    menu_task = page.locator("#mainFrame").content_frame.get_by_text("Red Local ►").hover()
    await asyncio.gather(click_task, hover_task, menu_task)

    content = await page.locator("span.popup hand").inner_html()
    print("Span HTML:", content)

    
    # await page.locator("#mainFrame").content_frame.get_by_text("Mapa red local").click()

    time.sleep(3)

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())