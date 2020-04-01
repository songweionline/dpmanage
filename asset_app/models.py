from django.db import models
from user_app.models import Plat, Department, Section, MyUser
from pj_manage.models import Project
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
    asset_user = models.ForeignKey('user_app.MyUser', verbose_name="使用人", on_delete=models.DO_NOTHING,
                                   related_name='asset_user')
    asset_charge_user = models.ForeignKey('user_app.MyUser', verbose_name="责任人", on_delete=models.DO_NOTHING,
                                          related_name='asset_charge_user')
    asset_operator = models.ForeignKey('user_app.MyUser', verbose_name='经办人', on_delete=models.DO_NOTHING,
                                       related_name='asset_operator')
    price = models.FloatField(null=True, verbose_name='价格')
    purchase_day = models.DateField(verbose_name='购买日期')
    expire_day = models.DateField(verbose_name='过保日期')
    memo = models.TextField(verbose_name='备注')

    def __str__(self):
        return '%s--%s--%s--%s' % (self.get_asset_type_display(), self.name, self.department, self.price)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = '资产总表'
        ordering = ['asset_id']


class Consumables(models.Model):   #耗材

    sub_type_choice = (
        (0, "电脑耗材"),
        (1, "蓝光盘"),
        (2, "数据流磁带"),
        (3, "视音频耗材"),
        (4, "其他耗材"),
    )
    project = models.ForeignKey('pj_manage.Project', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64, verbose_name='耗材名称')
    charge_user = models.ForeignKey('user_app.MyUser', verbose_name="责任人", on_delete=models.DO_NOTHING,
                                    related_name='charge_user')
    operator = models.ForeignKey('user_app.MyUser', verbose_name='经办人', on_delete=models.DO_NOTHING,
                                 related_name='operator')
    datetime = models.DateField(verbose_name='购买日期')
    price = models.IntegerField(verbose_name='单价')
    count = models.IntegerField(verbose_name='购买数量')
    has_Warranty = models.BooleanField(verbose_name='是否保修')
    warranty_time = models.DateField(verbose_name='保修日期')
    has_contract = models.BooleanField(verbose_name='是否签署合同')
    has_tender = models.BooleanField(verbose_name='是否招标')

    def __str__(self):
        return '<耗材名称:%s>--<单价:%s>--<购买数量:%s>--<责任人:%s>--<领用部门:%s>' % (self.name, self.price, self.count,
                                                                       self.charge_user, self.project.department)


'''class It(models.Model):
    it_type_choice = (
        (0, '服务器'),
        (1, '安全设备'),
        (2, '存储设备'),
        (3, '软件'),
    )
    asset = models.ForeignKey('Asset', max_length=64,)
    sub_it_type = models.SmallIntegerField(choices=it_type_choice, default=0, verbose_name='it设备类型')
'''