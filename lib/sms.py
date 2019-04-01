import random

import requests

from TanTan import config

def get_vcode(length=4):
    start = 10 ** (length - 1)
    end = 10 ** length
    return random.randint(start, end)

def send_sms(phonenum):
    vcode = str(get_vcode())
    url = config.YZX_SMS_API
    params = config.YZX_SMS_PARAMS
    params['param'] = vcode
    params['mobile'] = phonenum
    resp = requests.post(url, json=params)

    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return False, '短信服务器通信有误'


