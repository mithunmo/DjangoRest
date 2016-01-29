# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brandID', models.IntegerField()),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PortalProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectID', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('portalID', models.IntegerField()),
                ('createDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
