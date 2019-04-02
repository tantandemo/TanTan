import datetime

from django.db import models


class User(models.Model):
#  用户模型
    SEX = (
        ('male','男'),
        ('female','女')
    )
    phonenum = models.CharField(max_length=20, verbose_name='手机号')
    nickname = models.CharField(max_length=64, verbose_name='昵称')
    sex = models.CharField(choices=SEX,max_length=8, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='年')
    birth_month = models.IntegerField(default=1, verbose_name='月')
    birth_day = models.IntegerField(default=1, verbose_name='日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=16, verbose_name='长居地')

    class Meta:
        db_table = 'users'

    @property
    def age(self):
        today = datetime.date.today()
        birthday = datetime.date(year=self.birth_year, month=self.birth_month, day=self.birth_day)
        ages = (today - birthday).days // 365
        return ages


    # 将user对象转成字典型对象，在json_render()序列化
    def to_dict(self):
        return {
            'phonenum' : self.phonenum,
            'nickname':self.nickname,
            'sex':self.sex,
            # 'birth_year':self.birth_year,
            # 'birth_month':self.birth_month,
            # 'birth_day':self.birth_day,
            'age':self.age,
            'avatar':self.avatar,
            'location':self.location
        }