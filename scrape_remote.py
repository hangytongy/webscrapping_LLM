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

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body #get only the body content in the html
    if body_content: #if body content exists
        return str(body_content)
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]): #to remove all the scripting and styles in the html code [unnessasary characters]
        script_or_style.extract()
        
    cleaned_content = soup.get_text(seperator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()) 
    # get rid of "/n" characters that is not helping to seperate the texts
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i: i+ max_length] for i in range(0, len(dom_content), max_length)]
