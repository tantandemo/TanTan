from functools import wraps
from lib.http import render_json
from vip.models import Vip
from common import errors

def access(perm_name):
    def deco(func):
        @wraps(func)
        def wrap(request, *args, **kwargs):
            user = request.user
            vip = Vip.objects.get(level=user.permission_id)
            if vip.has_perm(perm_name):
                msg = func(request, *args, **kwargs)
                return render_json(msg)
            else:
                raise errors.Access_Err('权限不足！！！')
        return wrap
    return deco
