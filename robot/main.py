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

    # page.locator("#mainFrame").content_frame.locator("div").filter(has_text=re.compile(r"^ubuntu$")).first.click()
    # ip_address = page.locator("#mainFrame").content_frame.get_by_role("cell", name=re.compile(f"^192.168.1.\b")).first.inner_text()
    # print(f"TurtleBot3 IP address: {ip_address}")

    # page.locator("#mainFrame").content_frame.locator("div").filter(has_text=re.compile(r"^luisfeerxxo$")).first.click()
    # ip_address = page.locator("#mainFrame").content_frame.get_by_role("cell",  name=re.compile(f"^192.168.1.\b")).first.inner_text()
    # print(f"Remote PC IP address: {ip_address}")

    time.sleep(60)    

    # ---------------------
    context.close()
    browser.close()


# Remote PC: 192.168.1.37
# TurtleBot3: 192.168.1.39

with sync_playwright() as playwright:
    run(playwright)