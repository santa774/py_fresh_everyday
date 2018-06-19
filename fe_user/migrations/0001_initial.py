# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upasswd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('uphone', models.CharField(default=b'', max_length=11)),
                ('uaddress', models.CharField(default=b'', max_length=60)),
                ('ushou_name', models.CharField(default=b'', max_length=20)),
                ('uyoubian', models.CharField(default=b'', max_length=10)),
            ],
        ),
    ]
