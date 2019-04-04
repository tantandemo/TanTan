from django.db import models

class Vip(models.Model):
    """Vip表"""
    name = models.CharField(max_length=32, unique=True, verbose_name='会员名称')
    level = models.IntegerField(default=1, verbose_name='会员等级')
    price = models.FloatField(verbose_name='会员价格')

    @property
    def perm(self):
        vip_id_list = VipPermission.objects.filter(vip_id=self.id)
        perm_id_list = [vip_id_one.perm_id for vip_id_one in vip_id_list]
        _perm = Permission.objects.filter(id__in=perm_id_list)
        return _perm


    def has_perm(cls, perm_name):
        perms = cls.perm
        for perm in perms:
            if perm.name == perm_name:
                return True
        else:
            return False


class Permission(models.Model):
    """权限表"""
    name = models.CharField(max_length=32, unique=True, verbose_name='权限名称')
    description = models.TextField(verbose_name='权限描述')


class VipPermission(models.Model):
    vip_id = models.IntegerField(verbose_name='vip表id')
    perm_id = models.IntegerField(verbose_name='权限表id')