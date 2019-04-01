from django.http import JsonResponse
from django.core.cache import cache

from lib import sms
from lib import http
from user.models import User
from common import errors
from TanTan.forms import ProfileForm


def submit_phone(request):
    """提交手机号码"""
    phonenum = request.POST.get('phone')
    _, msg = sms.send_sms(phonenum)

    return http.render_json(data=msg)


def submit_vcode(request):
    """通过验证码登录、注册"""
    phonenum = request.POST.get('phone')
    vcode = request.POST.get('vcode')

    cache_code = cache.get(phonenum)
    print(cache_code)
    if vcode == cache_code:
        '''判断是登录还是注册'''
        try:
            user = User.objects.get(phonenum=phonenum)
        except:
            user = User.objects.create(phonenum=phonenum,nickname=phonenum)
        request.session['uid'] = user.id
        return http.render_json(data=user.to_dict())
    else:
        return http.render_json(data='验证码错误',code=errors.VCODE_ERR)


def get_profile(request):
    """获取个人资料"""
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    # print(user.profile)
    return http.render_json(user.profile.to_dict())

def edit_profile(request):
    """修改个人资料"""
    profileform = ProfileForm(request.POST)
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    if profileform.is_valid():
        # 接出对象，但不保存到数据库
        profile = profileform.save(commit=False)
        print(profile.to_dict())
        user.profile = profile
        profile.save()
        return http.render_json(profile.to_dict())
    else:
        return http.render_json(profileform.errors, errors.PROFILE__ERR)

def upload_avatar(request):
    """头像上"""
    pass
