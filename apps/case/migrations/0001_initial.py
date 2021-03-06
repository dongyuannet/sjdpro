# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-04 14:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resoucedit', '0006_auto_20190304_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='标题', max_length=255, verbose_name='标题')),
                ('image', models.ImageField(help_text='单张图', upload_to='actimage/%Y/%m/%d/', verbose_name='单张图')),
                ('start', models.DateTimeField(blank=True, help_text='开始时间', null=True, verbose_name='开始时间')),
                ('end', models.DateTimeField(blank=True, help_text='结束时间', null=True, verbose_name='结束时间')),
                ('reward_info', models.TextField(default='', help_text='奖品说明', verbose_name='奖品说明')),
                ('act_info', models.TextField(default='', help_text='活动说明', verbose_name='活动说明')),
                ('dui_info', models.TextField(default='', help_text='兑奖信息', verbose_name='兑奖信息')),
                ('intro', models.TextField(default='', help_text='机构介绍', verbose_name='机构介绍')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('effect', models.ForeignKey(blank=True, help_text='特效id', null=True, on_delete=django.db.models.deletion.CASCADE, to='resoucedit.Effects', verbose_name='特效id')),
                ('music', models.ForeignKey(blank=True, help_text='音乐id', null=True, on_delete=django.db.models.deletion.CASCADE, to='resoucedit.Music', verbose_name='音乐id')),
            ],
            options={
                'verbose_name_plural': '活动',
                'verbose_name': '活动',
            },
        ),
    ]
