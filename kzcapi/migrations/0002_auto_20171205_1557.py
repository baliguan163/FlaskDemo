# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-05 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kzcapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlasticBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plastic_type', models.CharField(choices=[('5x13', '默认胶框类型5x13'), ('10x13', '胶框类型0x13')], default='5x13', max_length=5, verbose_name='胶框类型')),
                ('plastic_carve_code', models.CharField(max_length=64, verbose_name='胶框刻码')),
                ('plastic_carve_scan_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='胶框扫码时间')),
                ('plastic_batter_over_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='胶框装完电池时间')),
                ('plastic_battery_check_pic_path', models.FileField(default='null', max_length=128, upload_to='', verbose_name='图像存储路径')),
                ('plastic_battery_check_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='图像生成日期')),
                ('plastic_battery_check_status', models.CharField(choices=[('0', '默认电池正反未检查'), ('1', 'CCD检测电池正反OK'), ('2', 'CCD检测电池正反NG'), ('3', '人工检测电池正反OK')], default='0', max_length=1, verbose_name='CCD检查状态')),
                ('plastic_battery_check_ng_scan_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='人工电池正反处理时间')),
                ('plastic_fixture_scan_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='人工扫码放夹具时间')),
                ('plastic_battery_soldering_data', models.CharField(default='null', max_length=128, verbose_name='模组焊接点数据')),
                ('plastic_battery_soldering_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='模组焊接时间')),
                ('plastic_soldering_a_check_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='模组A面焊接检查时间')),
                ('plastic_soldering_b_check_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='模组B面焊接检查时间')),
                ('plastic_soldering_a_check_status', models.CharField(choices=[('0', '默认焊接面未检查'), ('1', '焊接面检查OK'), ('2', '焊接面检查NG'), ('3', '焊接面人工处理检查OK')], default='0', max_length=1, verbose_name='A焊接面检查状态')),
                ('plastic_soldering_b_check_status', models.CharField(choices=[('0', '默认焊接面未检查'), ('1', '焊接面检查OK'), ('2', '焊接面检查NG'), ('3', '焊接面人工处理检查OK')], default='0', max_length=1, verbose_name='B焊接面检查状态')),
                ('plastic_soldering_ng_check_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='AB焊接面NG回流检查时间')),
                ('plastic_soldering_ab_check_static', models.CharField(choices=[('0', '默认焊接面未检查'), ('1', '焊接面检查OK'), ('2', '焊接面检查NG'), ('3', '焊接面人工处理检查OK')], default='0', max_length=1, verbose_name='AB焊接面NG回流检查状态')),
            ],
        ),
        migrations.AlterField(
            model_name='batchcode',
            name='batch_code_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='生成日期'),
        ),
        migrations.AlterField(
            model_name='ccdcheck',
            name='plastic_battery_check_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='生成日期'),
        ),
        migrations.AlterField(
            model_name='ccdcheck',
            name='plastic_battery_check_pic_path',
            field=models.FileField(default='null', max_length=128, upload_to='', verbose_name='图像路径'),
        ),
        migrations.AlterField(
            model_name='ccdcheck',
            name='plastic_battery_check_status',
            field=models.CharField(choices=[('0', '默认电池正反未检查'), ('1', 'CCD检测电池正反OK'), ('2', 'CCD检测电池正反NG'), ('3', '人工检测电池正反OK')], default='0', max_length=1, verbose_name='检查状态'),
        ),
        migrations.AlterField(
            model_name='ccdcheck',
            name='plastic_carve_code',
            field=models.CharField(max_length=64, verbose_name='胶框刻码'),
        ),
    ]
