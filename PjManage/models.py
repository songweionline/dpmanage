from django.db import models
from django.contrib.auth.models import User
# Create your models here.


'''class Project(models.Model):

    """ 所有项目共有属性  """

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

    project_price_area = models.CharField(choices=project_price_area_choice, max_length=64, default='sporadic', verbose_name="采购方式")
    name = models.CharField(max_length=128, verbose_name="项目名称")
    manufacturer = models.CharField'''