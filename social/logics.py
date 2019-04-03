import datetime

from django.core.cache import cache

from user.models import User
from social.models import Swiped
from social.models import Friend
from common import keys
from TanTan import config
from common import errors


def return_rcmd_list(user):
    swiped = Swiped.objects.filter(uid=user.id).only('sid')
    swiped_sid_list = [sw.id for sw in swiped]
    # 把自己添加进去
    swiped_sid_list.append(user.id)

    today = datetime.date.today().year
    min_age = today - user.profile.max_dating_age
    max_age = today - user.profile.min_dating_age


    users = User.objects.filter(location=user.profile.location,
                        birth_year__range=[min_age,max_age],
                        sex=user.profile.dating_sex,
                        ).exclude(id__in=swiped_sid_list)[:20]

    return users


def like(user, sid, mark):
    Swiped.create_swiped(user, sid, mark)

    if Swiped.objects.filter(uid=sid, sid=user.id).exists():
        Friend.create_friend(user, sid)
        # TODO 通知对方好友关系已经建立，可以开始聊天了
        msg = '建立好友关系'
    else:
        msg = '啥也没'
    return msg

def rewind(user):
    now = datetime.datetime.now()
    key = keys.REWIND_KEY % (user.id, now.date())

    rewind_times = cache.get(key, 0)

    if rewind_times < config.REWIND_TIMES:
        # 反悔操作
        swiped = Swiped.objects.filter(uid=user.id).latest('time')
        uid1, uid2 = (user.id, swiped.sid) if user.id < swiped.sid else (swiped.sid, user.id)
        print(uid1, uid2)

        friend = Friend.objects.filter(uid1=uid1, uid2=uid2)
        print(friend)
        friend.delete()
        swiped.delete()

        # 重新加入到缓存
        rewind_times += 1
        print(rewind_times)
        timeout = 86400 - (now.hour * 3600 + now.minute*60 + now.second)
        cache.set(key, rewind_times, timeout)
        return True

    else:
        raise errors.RewindLimit('超出最大次数')
