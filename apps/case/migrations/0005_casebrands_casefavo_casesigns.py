# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-04 15:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_acts_cate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseBrands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='名称', max_length=255, verbose_name='名称')),
                ('location_x', models.FloatField(default='', help_text='经度', verbose_name='经度')),
                ('location_y', models.FloatField(default='', help_text='纬度', verbose_name='纬度')),
                ('address', models.CharField(default='', help_text='具体地址', max_length=255, verbose_name='具体地址')),
                ('phones', models.CharField(default='', help_text='手机号组', max_length=255, verbose_name='手机号组')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('case', models.ForeignKey(blank=True, help_text='案例id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_case_brands', to='case.Acts', verbose_name='案例id')),
            ],
            options={
                'verbose_name': '门店信息',
                'verbose_name_plural': '门店信息',
            },
        ),
        migrations.CreateModel(
            name='CaseFavo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='名称', max_length=255, verbose_name='名称')),
                ('sort', models.IntegerField(default=1, help_text='排序', verbose_name='排序')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('case', models.ForeignKey(blank=True, help_text='案例id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_cases', to='case.Acts', verbose_name='案例id')),
            ],
            options={
                'verbose_name': '优惠信息',
                'verbose_name_plural': '优惠信息',
            },
        ),
        migrations.CreateModel(
            name='CaseSigns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='名称', max_length=255, verbose_name='名称')),
                ('value', models.CharField(default='', help_text='值', max_length=255, verbose_name='值')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('case', models.ForeignKey(blank=True, help_text='案例id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_case_signs', to='case.Acts', verbose_name='案例id')),
            ],
            options={
                'verbose_name': '报名信息',
                'verbose_name_plural': '报名信息',
            },
        ),
    ]
