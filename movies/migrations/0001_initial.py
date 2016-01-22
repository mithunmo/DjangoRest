# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shortDesc', models.CharField(max_length=200)),
                ('productionYear', models.CharField(max_length=4)),
                ('longDesc', models.TextField()),
                ('moderatorComments', models.TextField(null=True)),
                ('uploaded', models.DateTimeField(verbose_name=b'date published')),
                ('modified', models.DateTimeField(verbose_name=b'date published')),
                ('moderated', models.DateTimeField(null=True, verbose_name=b'date published')),
                ('userID', models.IntegerField(default=0)),
                ('private', models.IntegerField(default=0)),
                ('avgRating', models.IntegerField(default=0)),
                ('ratingCount', models.IntegerField(default=0)),
                ('runtime', models.IntegerField(default=0)),
                ('moderatorID', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100)),
                ('active', models.CharField(max_length=100)),
                ('credits', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='MovieSources',
            fields=[
                ('movies', models.ForeignKey(related_name='movieSources', primary_key=True, db_column=b'movieID', serialize=False, to='quickstart.movies')),
                ('sourceID', models.IntegerField(db_column=b'sourceID')),
            ],
            options={
                'db_table': 'movieSources',
            },
        ),
    ]
