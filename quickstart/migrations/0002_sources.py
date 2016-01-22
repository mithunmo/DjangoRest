# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('sourceID', models.ForeignKey(related_name='sources', primary_key=True, db_column=b'id', serialize=False, to='quickstart.MovieSources')),
                ('eventID', models.IntegerField(db_column=b'eventID')),
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
            ],
            options={
                'db_table': 'sources',
            },
        ),
    ]
