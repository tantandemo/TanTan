from django.db import models


class Swiped(models.Model):
    MAEKS = (
        ('dislike', '左滑'),
        ('like', '右滑'),
        ('superlike', '上滑'),
    )
    uid = models.IntegerField(verbose_name='用户自身 id')
    sid = models.IntegerField(verbose_name='被滑的陌生人 id')
    mark = models.CharField(choices=MAEKS, max_length=20, verbose_name='滑动类型')
    time = models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')
