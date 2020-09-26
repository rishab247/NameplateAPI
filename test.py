from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument('headless')
# print(time.time()-start)
import os
os.system('ls')
browser = webdriver.Chrome( executable_path= r'/home/site/wwwroot/chromedriver1',options = option)
