from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')

browser = webdriver.Chrome(options=option)
browser.get('https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml')

plateNumber = ""
captchaAnswer = ""

browser.find_element_by_xpath('//*[@id="regn_no1_exact"]').send_keys(str(plateNumber))
browser.find_element_by_xpath('//*[@id="txt_ALPHA_NUMERIC"]').send_keys(str(captchaAnswer))
browser.find_element_by_class_name("ui-button-text").click()
print("Printing Title of the Wepage visited")
print(browser.title)