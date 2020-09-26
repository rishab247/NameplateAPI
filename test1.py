from selenium import webdriver


import os
os.system('ls')
o = webdriver.ChromeOptions()
o.add_argument("--headless")
o.add_argument("--disable-gpu")
o.add_argument("--no-sandbox")
o.add_argument("enable-automation")
o.add_argument("--disable-infobars")
o.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome( executable_path= r'/home/site/wwwroot/chromedriver.exe',options = o)
try:
    browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
    print(browser.title)
    browser.close()
except Exception as e :
    print(e)
    browser.close()



#
# from selenium import webdriver
# # Option 1 - with ChromeOptions
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
# driver = webdriver.Chrome(driver_path=r'/mnt/d/SD(SE)/university-project/Nameplate project/chromedriver2', chrome_options=chrome_options,
#   service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
#
#
