from playwright.sync_api import sync_playwright 

centre_index = 1 # Edinburgh = 0, London = 1, Manchester = 2
email = "usvi980@outlook.com" # Account email
password = "123456Asdfgh!" # Account password

with sync_playwright() as pw:
    browser = pw.firefox.launch(
        headless=True,  # Set to False if you want to see the browser
        slow_mo=2000
    )

    page = browser.new_page()
    
    # Initial page
    page.goto("https://visas-fr.tlscontact.com/country/gb/?lang=en-us")
    page.wait_for_load_state("load")
    print("Centre Selection Page Loaded")
    page.screenshot(path="screenshots/Centre Selection.png")

    # Navigate to preferred centre
    with page.expect_navigation():
        page.get_by_role("button").get_by_text("Continue").nth(centre_index).click()
    page.wait_for_load_state("load")
    print("Centre Home Page Loaded")
    page.screenshot(path="screenshots/Centre Home.png")

    browser.close()