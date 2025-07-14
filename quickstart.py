from playwright.sync_api import sync_playwright 

pw = sync_playwright().start()

browser = pw.firefox.launch()

page = browser.new_page()
page.goto("https://www.google.com")

print(page.content())
print(page.title())
page.screenshot(path="screenshot.png")

browser.close()