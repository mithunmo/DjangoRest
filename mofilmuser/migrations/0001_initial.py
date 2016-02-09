# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MofilmUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'ID')),
                ('clientid', models.IntegerField(null=True, db_column=b'clientID', blank=True)),
                ('password', models.CharField(max_length=32, null=True, blank=True)),
                ('email', models.CharField(max_length=70)),
                ('enabled', models.CharField(max_length=1)),
                ('territoryid', models.IntegerField(null=True, db_column=b'territoryID', blank=True)),
                ('facebookid', models.BigIntegerField(null=True, db_column=b'facebookID', blank=True)),
                ('firstname', models.CharField(max_length=50, null=True, blank=True)),
                ('surname', models.CharField(max_length=50, null=True, blank=True)),
                ('registered', models.DateTimeField(auto_now=True)),
                ('regip', models.CharField(max_length=15, null=True, db_column=b'regIP', blank=True)),
                ('hash', models.CharField(max_length=32, unique=True, null=True, blank=True)),
                ('autocommitstatus', models.IntegerField(null=True, db_column=b'autoCommitStatus', blank=True)),
                ('userrole', models.IntegerField(db_column=b'userRole')),
                ('proenabled', models.IntegerField(db_column=b'proEnabled')),
                ('proonly', models.IntegerField(db_column=b'proOnly')),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
