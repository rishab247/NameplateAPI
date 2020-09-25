import pypyodbc
from flask import Flask, jsonify, request, make_response, logging
import jwt
import json
import datetime
from selenium import webdriver
import sys
import base64

from webdrivermanager import GeckoDriverManager
import urllib.request
import time
from functools import wraps

app = Flask(__name__)

app.config[
    'SECRET_KEY'] = 'supsd3123xdf3232c32s32a3s'



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.args.get('token')
        if not token:
            return jsonify({'msg': 'token req', }), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'msg': 'token is not valid', }), 401
        return f(data, *args, **kwargs)

    return decorated









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



@app.route('/verify', methods=['POST'])
def verify():

    # starting time
    start = time.time()

    print(time.time() - start)
    browser.get('https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml')
    print(time.time() - start)
    plateNumber = ""
    captchaAnswer = ""

    # captcha selector tag : //*[@id="form_rcdl:j_idt32:j_idt37"]

    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no1"]').send_keys(plateNumber[:-4])
    browser.find_element_by_xpath('//*[@id="form_rcdl:tf_reg_no2"]').send_keys(plateNumber[-4:])
    browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:CaptchaID"]').send_keys(captchaAnswer)
    print(time.time() - start)

    # browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').
    img = browser.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt37"]').get_attribute('src')
    print(img)
    print(time.time() - start)
    urllib.request.urlretrieve(img, "captcha.png")
    z = base64.b64encode(urllib.request.urlopen(img).read())
    # print(sys. getsizeof(browser))
    return jsonify({'msg': str(z[2:-1])}), 200


@app.route('/getdetails', methods=['POST'])
def getdetails():
    jsondata = request.get_data().decode("utf-8")
    jsondata = json.loads(jsondata)

    return jsonify({'msg': jsondata['code']}), 200
@app.route('/')
def About():
    return jsonify({'About': 'STUFFFF'}), 200




if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # print(time.time()-start)
    browser = webdriver.Chrome(options=option)
    app.run()
