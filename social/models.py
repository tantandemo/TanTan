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

    @classmethod
    def create_swiped(cls, user, sid, mark='like'):
        if not Swiped.objects.filter(uid=user.id, sid=sid).exists():
            swiped = Swiped.objects.create(uid=user.id, sid=sid, mark=mark)
            return True


class Friend(models.Model):
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def create_friend(cls, user, sid):
        uid1, uid2 =(user.id, sid) if user.id < sid else (sid, user.id)
        if not Friend.objects.filter(uid1=uid1, uid2=uid2).exists():
            Friend.objects.create(uid1=uid1, uid2=uid2)
