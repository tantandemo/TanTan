from django.core.cache import cache
from django.shortcuts import render
from django.http import JsonResponse

from TanTan import config
from common import keys, errors
from common.keys import AVATAR_KEY
from lib.sendsms import send_sms
from lib.http import render_json
from user.models import User


def submit_phone(request):
    # 提交手机号码
    phone_num = request.POST.get('phone')
    print(phone_num)
    # 拿到手机号去发短信
    send_sms(phone_num)
    return render_json(data=None, code=0)



def submit_sms_code(request):
    # 通过验证码登录、注册
    phone_num = request.POST.get('phone')
    vcode = request.POST.get('vcode')
    cached_v_code = cache.get(keys.VCODE_KEY % phone_num)
    if vcode == cached_v_code:
        # 登录和注册
        # 如果能从数据库查到用户，则是注册过的
        # try:
        #     User.objects.get(phone_num=phone_num)
        # except User.DoesNotExist:
        #     # 是注册
        #     User.objects.create(phone_num=phone_num)
        # 简化
        user, _ = User.objects.get_or_create(phonenum=phone_num, nickname=phone_num)
        # 不管登录注册，得到数据后登录
        request.session['uid'] = user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(data='验证码有误', code=errors.VCODE_ERR)


def get_profile(request):
    # 获取个人资料
    uid = request.session['uid']
    user = User.objects.get(id=uid)

    return render_json(user.profile.to_dict())


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

