from django.db import models
from django.contrib.auth.models import User
from user_app.models import Plat, Department, Section
# Create your models here.


class Asset(models.Model):  #资产共有属性
    asset_type_choice = (
        ('it_device', 'it设备'),
        ('video', '视频设备'),
        ('audio', '音频设备'),
        ('other', '其他设备'),
    )

    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
        (5, '待报废'),
        (6, '报废'),
    )

    asset_type = models.CharField(choices=asset_type_choice, max_length=64, verbose_name='资产类型')
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='资产状态')
    name = models.CharField(max_length=128, verbose_name='资产名称')
    sn = models.CharField(max_length=128, verbose_name='资产序列号')
    asset_id = models.IntegerField(verbose_name='资产编号')
    department = models.ForeignKey('user_app.Department', verbose_name='所属部门', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('user_app.MyUser', verbose_name="使用人", on_delete=models.DO_NOTHING)
    charge_user = models.ForeignKey('user_app.MyUser', verbose_name="责任人", on_delete=models.DO_NOTHING)
    operator = models.ForeignKey('user_app.MyUser', verbose_name='经办人', on_delete=models.DO_NOTHING)
    price = models.FloatField(null=True, verbose_name='价格')
    purchase_day = models.DateField(verbose_name='购买日期')
    expire_day = models.DateField(verbose_name='过保日期')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='品牌',
                                     on_delete=models.SET_NULL)
    memo = models.TextField(verbose_name='备注')

    def __str__(self):
        return '<%s>--%s--%s--%s--%s--%s' % (self.get_asset_type_display(), self.name, self.department, self.user,
                                             self.charge_user, self.price)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = '资产总表'
        ordering = ['asset_id']


class It(models.Model):
    it_type_choice = (
        (0, '服务器'),
        (1, '安全设备'),
        (2, '存储设备'),
        (3, '软件'),
    )
    asset = models.ForeignKey('Asset', max_length=64,)
    sub_it_type = models.SmallIntegerField(choices=it_type_choice, default=0, verbose_name='it设备类型')
