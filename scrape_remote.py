from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup


SBR_WEBDRIVER = "https://brd-customer-hl_....." #remote broswer instance

def scrape_web(website):
    print("launching chrome browser")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER,'goog','chrome') #connecting to remote browser
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("waiting to solve captcha")
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scrapping page...')
        html = driver.page_source
        return html