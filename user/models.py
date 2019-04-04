import datetime

from django.db import models

from lib.orm import ModelMixin
from social.models import Friend,Swiped

class User(models.Model):
    SEX = (
        ('male','男'),
        ('female','女'),
    )

    phonenum = models.CharField(max_length=20, verbose_name='手机号')
    nickname = models.CharField(max_length=64, verbose_name='昵称')
    sex = models.CharField(choices=SEX, max_length=100, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=20, verbose_name='常居地')

    # 权限
    permission_id = models.IntegerField(default=0, verbose_name='权限等级')

    class Meta:
        db_table = 'user'

    @property
    def age(self):
        birth = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        today = datetime.date.today()
        return (today - birth).days//365

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    @property
    def get_liked_me(self):
        user_id_list = Swiped.liked_me_list(self)
        users = User.objects.filter(id__in=user_id_list)
        return users
    @property
    def friends(self):
        friends_list = Friend.get_friends(self)
        users = User.objects.filter(id__in=friends_list)
        return users

    def to_dict(self):
        return {
            "phonenum": self.phonenum,
            "nickname": self.nickname,
            "sex": self.sex,
            "age": self.age,
            "avatar": self.avatar,
            "location": self.location,
        }


class Profile(models.Model, ModelMixin):
    SEX = (
        ('male', '男'),
        ('female', '女'),
    )

    location = models.CharField(max_length=100, verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=50, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    dating_sex = models.CharField(choices=SEX, max_length=8, verbose_name='匹配的性别')
    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')










