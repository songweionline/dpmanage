from django.db import models
from django.contrib.auth.models import User
from user_app.models import Plat, Department, Section
# Create your models here.


class Project(models.Model):  #共有属性

    project_price_area_choice = (
        ('sporadic', '1万以内零星采购'),
        ('inquiry', '1-10万询价采购'),
        ('internal', '10-30万内部招标'),
        ('public', '30万以上公开招标'),
    )

    project_type_choice = (
        ('consumables', '耗材'),
        ('service', '维修'),
        ('maintain', '维保'),
        ('protocol', '政府协议供货'),
        ('blu_rayDisc', '蓝光盘'),
        ('tape', '数据流磁带'),
        ('operations', '技术运营'),
    )

    project_price_area = models.CharField(choices=project_price_area_choice, max_length=64, verbose_name="采购方式")
    project_type = models.CharField(choices=project_type_choice, max_length=64, verbose_name='采购类型')
    name = models.CharField(max_length=128, verbose_name="项目名称")
    manufacturer = models.CharField(max_length=128, verbose_name="供应商名称")
    department = models.ForeignKey('user_app.Department', verbose_name="所属部门", on_delete=models.DO_NOTHING)
    budget = models.FloatField(verbose_name='项目预算')
    price = models.FloatField(verbose_name='项目总价')

    def __str__(self):
        return '<项目名称:%s>--<项目预算:%s>--<项目金额:%s>--<所属部门:%s>' % (self.name, self.budget, self.price,
                                                               self.department)

    class Meta:
        verbose_name = '项目总表'
        verbose_name_plural = '项目总表'


class Consumables(models.Model):   #耗材

    sub_type_choice = (
        (0, "电脑耗材"),
        (1, "蓝光盘"),
        (2, "数据流磁带"),
        (3, "视音频耗材"),
        (4, "其他耗材"),
    )
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64, verbose_name='耗材名称')
    user = models.ForeignKey('user_app.MyUser', verbose_name="使用人", on_delete=models.DO_NOTHING)
    charge_user = models.ForeignKey('user_app.MyUser', verbose_name="责任人", on_delete=models.DO_NOTHING)
    operator = models.ForeignKey('user_app.MyUser', verbose_name='经办人', on_delete=models.DO_NOTHING)
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

    class Meta:
        verbose_name = '耗材总表'
        verbose_name_plural = '耗材总表'



