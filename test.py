from webdrivermanager import ChromeDriverManager
from selenium import webdriver
# import cv2 as cv
import urllib.request
import time

gdd = ChromeDriverManager()
gdd.download_and_install()

option = webdriver.ChromeOptions()
option.add_argument('headless')
# print(time.time()-start)
browser = webdriver.Chrome(options=option)