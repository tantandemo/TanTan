"""各种错误码"""

# 验证码错误
VCODE_ERR = 1001

# 数据错误
PROFILE__ERR = 1002

# 需要登录
LOGIN_REGISTERD = 1004

class LogicErr(Exception):
    code = None
    data = None

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.__class__.__name__


# 生成异常类工厂
def gen_logic_err(name, code):
    att_dict = {'code': code}
    return type(name, (LogicErr,), att_dict)

VcodeErr = gen_logic_err('VcodeErr', 1001)
ProfileErr = gen_logic_err('ProfileErr', 1002)
LoginRegisterd = gen_logic_err('LoginRegisterd', 1004)
RewindLimit = gen_logic_err('RewindLimit', 1005)