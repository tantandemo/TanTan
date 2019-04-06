# 发送短信
import random

import requests
from django.core.cache import cache

from TanTan import config
from common import keys


def gen_sms_code(length=6):
    start = 10 ** (length - 1)
    end = 10 ** length -1
    vcode = random.randint(start,end)
    return vcode


def send_sms(phone_num):
    sms_code = gen_sms_code()
    cache.set(keys.VCODE_KEY % phone_num, str(sms_code), 300)
    url = config.YZX_SMS_API
    params = config.YZX_SMS_PARAMS.copy()
    params['param'] = sms_code
    params['mobile'] = phone_num
    response = requests.post(url, json=params)
    # response.json()

    # 检查结果
    if response.status_code == 200:
        result = response.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return '短信服务器无法连接'