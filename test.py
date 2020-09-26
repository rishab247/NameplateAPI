from selenium import webdriver


options = webdriver.ChromeOptions()
import os
os.system('ls')
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome( executable_path= r'/mnt/d/SD(SE)/university-project/Nameplate project/chromedriver2',options = options)
try:
    browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
    print(browser.title)
    browser.close()
except Exception as e :
    print(e)
    browser.close()