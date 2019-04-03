from social.logics import return_rcmd_list
from lib.http import render_json


def get_rcmd_list(request):
    """获取推荐列表"""
    user = request.user
    users = return_rcmd_list(user)
    data = [one.to_dict() for one in users]
    return render_json(data)

def like(request):
    """喜欢"""
    pass

def superlike(request):
    """超级喜欢"""
    pass

def dislike(request):
    """不喜欢"""
    pass

def rewind(request):
    """反悔(每天允许返回 3 次)"""
    pass

def get_liked_list(request):
    """查看喜欢过我的人"""
    pass


