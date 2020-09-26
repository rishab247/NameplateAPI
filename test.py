from selenium import webdriver


options = webdriver.ChromeOptions()
import os
os.system('ls')
browser = webdriver.Chrome( executable_path= r'/mnt/d/SD(SE)/university-project/Nameplate project/chromedriver1',options = options)
browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
print(browser.title)
browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys("[:-4]")
