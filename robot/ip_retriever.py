import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    
    page.goto("https://192.168.1.1")
    page.locator("#mainFrame").content_frame.get_by_role("textbox").click()
    page.locator("#mainFrame").content_frame.get_by_role("textbox").fill("#330844@ED00F7*")
    page.locator("#mainFrame").content_frame.get_by_role("button", name="Entrar").click()
    page.locator("#mainFrame").content_frame.get_by_role("cell", name="MENU").click()
    page.locator("#mainFrame").content_frame.get_by_text("Red Local ► Mapa red local").hover()
    page.locator("#mainFrame").content_frame.get_by_text("Red Local ►").click()
    page.locator("#mainFrame").content_frame.get_by_text("Mapa red local").click()


    time.sleep(60)    

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


# Remote PC: 192.168.1.80
# TurtleBot3: 192.168.1.79