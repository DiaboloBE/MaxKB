# Generated by Django 4.2.18 on 2025-03-25 03:22

import common.encoder.encoder
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0009_set_default_model_params_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, verbose_name='主键id')),
                ('menu', models.CharField(max_length=128, verbose_name='操作菜单')),
                ('operate', models.CharField(max_length=128, verbose_name='操作')),
                ('operation_object', models.JSONField(default=dict, encoder=common.encoder.encoder.SystemEncoder, verbose_name='操作对象')),
                ('user', models.JSONField(default=dict, verbose_name='用户信息')),
                ('status', models.IntegerField(verbose_name='状态')),
                ('ip_address', models.CharField(max_length=128, verbose_name='ip地址')),
                ('details', models.JSONField(default=dict, encoder=common.encoder.encoder.SystemEncoder, verbose_name='详情')),
            ],
            options={
                'db_table': 'log',
            },
        ),
    ]
