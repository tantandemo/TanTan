from django.db import models


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

    class Meta:
        db_table = 'user'