from django.shortcuts import render
from django.http import JsonResponse
from lib import sms

def submit_phone(request):
    """提交手机号码"""
    phonenum = request.POST.get('phone')
    _, msg = sms.send_sms(phonenum)

    return JsonResponse({'data': None, 'code': 0, 'msg': msg})

def submit_vcode(request):
    """通过验证码登录、注册"""
    pass

def get_profile(request):
    """获取个人资料"""
    pass

def edit_profile(request):
    """修改个人资料"""
    pass

def upload_avatar(request):
    """头像上"""
    pass
