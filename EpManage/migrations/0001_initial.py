# Generated by Django 3.0.3 on 2020-03-29 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_id', models.SmallIntegerField(null=True, verbose_name='部门编号')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '部门总表',
                'verbose_name_plural': '部门总表',
            },
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_id', models.SmallIntegerField(null=True, verbose_name='平台编号')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='平台名称')),
            ],
            options={
                'verbose_name': '平台总表',
                'verbose_name_plural': '平台总表',
                'ordering': ['pt_id'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.SmallIntegerField(verbose_name='科室编号')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='科室名称')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EpManage.Department', verbose_name='所属部门')),
            ],
            options={
                'verbose_name': '科室总表',
                'verbose_name_plural': '科室总表',
            },
        ),
        migrations.CreateModel(
            name='EpProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.SmallIntegerField(null=True, unique=True, verbose_name='员工编号')),
                ('phone', models.CharField(max_length=64, verbose_name='电话号码')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EpManage.Department', verbose_name='所属部门')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EpManage.Section', verbose_name='所属科室')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='员工总表')),
            ],
            options={
                'verbose_name': '员工总表',
                'verbose_name_plural': '员工总表',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='plat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EpManage.Plat', verbose_name='所属平台'),
        ),
    ]
