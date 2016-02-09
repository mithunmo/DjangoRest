# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
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
            name='PortalContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portalID', models.IntegerField()),
                ('contentType', models.CharField(max_length=100)),
                ('licenseTerms', models.TextField()),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('movies', models.OneToOneField(db_column=b'movies_id', to='movies.Movie')),
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
        migrations.CreateModel(
            name='PortalUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'ID')),
                ('portalID', models.ForeignKey(to='portal.Portal')),
                ('userID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
