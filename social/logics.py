import datetime

from user.models import User
from social.models import Swiped


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
