import datetime

from django.core.cache import cache

from social import logics
from lib.http import render_json
from social.models import Swiped
from social.models import Friend
from common import keys
from TanTan import config


def get_rcmd_list(request):
    """获取推荐列表"""
    user = request.user
    users = logics.return_rcmd_list(user)
    data = [one.to_dict() for one in users]
    return render_json(data)

def like(request):
    """喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    msg = logics.like(user, sid, 'like')
    return render_json(msg)

def superlike(request):
    """超级喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    msg = logics.like(user, sid, 'superlike')
    return render_json(msg)

def dislike(request):
    """不喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    result = Swiped.create_swiped(user, sid, 'dislike')
    return render_json(result)


def rewind(request):
    """反悔(每天允许返回 3 次)"""
    user = request.user
    result = logics.rewind(user)

    return render_json(result)


def get_liked_list(request):
    """查看喜欢过我的人"""
    pass


