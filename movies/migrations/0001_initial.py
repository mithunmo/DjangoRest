# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('productID', models.IntegerField()),
                ('termsID', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('webpath', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('hidden', models.CharField(max_length=50)),
                ('tba', models.CharField(max_length=50)),
                ('custom', models.CharField(max_length=50)),
                ('instructions', models.TextField()),
                ('bgcolor', models.CharField(max_length=10)),
                ('startDate', models.DateTimeField(verbose_name=b'date published')),
                ('endDate', models.DateTimeField(verbose_name=b'date published')),
                ('awardstartDate', models.DateTimeField(verbose_name=b'date published')),
                ('awardendDate', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Movie',
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
            name='MovieSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movieID', models.ForeignKey(related_name='movieSources', db_column=b'movieID', to='movies.Movie')),
            ],
            options={
                'db_table': 'movieSources',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brandID', models.IntegerField(db_column=b'brandID')),
                ('sponsorID', models.IntegerField(db_column=b'sponsorID')),
                ('termsID', models.IntegerField(db_column=b'termsID')),
                ('tripBudget', models.IntegerField(db_column=b'tripBudget')),
                ('name', models.CharField(max_length=40)),
                ('webfilename', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('hidden', models.CharField(max_length=50)),
                ('custom', models.CharField(max_length=50)),
                ('instructions', models.TextField()),
                ('bgcolor', models.CharField(max_length=10)),
                ('startDate', models.DateTimeField(verbose_name=b'date published')),
                ('endDate', models.DateTimeField(verbose_name=b'date published')),
                ('closeDate', models.DateField()),
                ('createdDate', models.DateTimeField()),
                ('events', models.OneToOneField(db_column=b'eventID', to='movies.Event')),
                ('movies', models.ManyToManyField(related_name='sources', through='movies.MovieSource', to='movies.Movie')),
            ],
            options={
                'db_table': 'sources',
            },
        ),
        migrations.AddField(
            model_name='moviesource',
            name='sourceID',
            field=models.ForeignKey(related_name='movieSources', db_column=b'sourceID', to='movies.Source'),
        ),
    ]
