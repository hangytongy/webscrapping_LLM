import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

def scrape_web(website):
    print("launching chrome browser")
    
    #https://googlechromelabs.github.io/chrome-for-testing/#stable
    #extract chrome driver and copy the application into this directory
    
    chrome_driver_path = "./chromedriver" #path to the chrome driver application
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
    chrome_options.add_argument("--no-sandbox")  # Required for some environments
    chrome_options.add_argument("--disable-dev-shm-usage") 
    
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    try:
        driver.get(website)
        print("page loaded")
        html = driver.page_source
        time.sleep(10)
        
        return html
    
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body #get only the body content in the html
    if body_content: #if body content exists
        return str(body_content)
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]): #to remove all the scripting and styles in the html code [unnessasary characters]
        script_or_style.extract()
        
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()) 
    # get rid of "/n" characters that is not helping to seperate the texts
    
    return cleaned_content

def split_dom_content(dom_content, max_length=100000):
    return [dom_content[i: i+ max_length] for i in range(0, len(dom_content), max_length)]
