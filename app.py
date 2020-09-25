from flask import Flask, jsonify, request, make_response, logging
import json
from selenium import webdriver
import base64
import urllib.request
import time
import os
from selenium.webdriver.chrome.options import Options


app = Flask(__name__)



# @app.route('/start', methods=['POST'])
# def start():
#
#     # starting time
#     start = time.time()
#
#     print(time.time() - start)
#     browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
#     print(time.time() - start)
#     plateNumber = ""
#     captchaAnswer = ""
#
#     # captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]
#
#     browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
#     browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
#     browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
#     print(time.time() - start)
#
#     # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
#     img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
#     print(img)
#     print(time.time() - start)
#     urllib.request.urlretrieve(img, "captcha.png")
#     z = base64.b64encode(urllib.request.urlopen(img).read())
#     # print(sys. getsizeof(browser))
#     return jsonify({'msg': str(z)}), 200
#
#



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
@app.route('/verify', methods=['POST'])
def verify():
    try:
        chrome_options.add_argument('headless')

        browser = webdriver.Chrome(options=chrome_options)
        app.logger.info('test4')
        # starting time
        start = time.time()

        app.logger.info('test5')
        print(time.time() - start)
        browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
        print(time.time() - start)
        plateNumber = ""
        captchaAnswer = ""

        app.logger.info('test6')
        # captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]

        browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
        browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
        browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
        print(time.time() - start)

        app.logger.info('test6')
        # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
        img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
        print(img)
        print(time.time() - start)
        urllib.request.urlretrieve(img, "captcha.png")
        z = base64.b64encode(urllib.request.urlopen(img).read())
        # print(sys. getsizeof(browser))
        return jsonify({'msg': str(z[2:-1])}), 200
    except Exception as e :
        return jsonify({'msg': str(e)}), 200


@app.route('/getdetails', methods=['POST'])
def getdetails():
    app.logger.info('test2')
    jsondata = request.get_data().decode("utf-8")
    jsondata = json.loads(jsondata)

    return jsonify({'msg': jsondata['code']}), 200
@app.route('/')
def About():
    app.logger.info('test1')
    return jsonify({'About': 'STUFFFF'}), 200




if __name__ == '__main__':

    app.run(debug=True)
