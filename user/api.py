from django.shortcuts import render
from django.http import JsonResponse

from common.keys import AVATAR_KEY
from lib.sendsms import send_sms
from lib.http import render_json


def submit_phone(request):
    # 提交手机号码
    phone_num = request.POST.get('phone')
    print(phone_num)
    # 拿到手机号去发短信
    send_sms(phone_num)
    return JsonResponse({'data':None,'code':0})



def submit_sms_code(request):
    # 通过验证码登录、注册
    return


def get_profile(request):
    # 获取个人资料
    return


def edit_profile(request):
    #  修改个人资料
    return


def upload_avatar(request):
    # 头像上传
    avatar = request.FILES.get('avatar')
    # print(avatar)
    uid = request.session['uid']
    with open('midels/'+ AVATAR_KEY % uid, 'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    return render_json(None)

