from playwright.sync_api import sync_playwright 

pw = sync_playwright().start()

browser = pw.firefox.launch(
    headless=False,  # Set to False if you want to see the browser
    # slow_mo=2000
)

page = browser.new_page()
page.goto("https://www.google.com")

print(page.content())
print(page.title())
page.screenshot(path="screenshot.png")

browser.close()