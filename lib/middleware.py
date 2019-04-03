from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import render_json
from common.errors import LOGIN_REGISTERD
from common.errors import LogicErr


class AuthMiddleware(MiddlewareMixin):
    # 请求的路径白名单
    URL_WHITE_LIST = [
        '/api/submit/phone/',
        '/api/submit/vcode/',
    ]

    def process_request(self, request):
        if request.path in self.URL_WHITE_LIST:
            return

        uid = request.session.get('uid')
        if uid:
            user = User.objects.get(id=uid)
            request.user = user
            return
        else:
            return render_json('请登录', LOGIN_REGISTERD)

class LogicErrMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # 判断是不是自己定义的异常
        # print(exception)
        if isinstance(exception, LogicErr):
            # print(exception.data)
            # print(exception.code)
            return render_json(exception.data, exception.code)
