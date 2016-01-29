# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portalID', models.IntegerField()),
                ('contentType', models.CharField(max_length=100)),
                ('licenseTerms', models.TextField()),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('movies', models.OneToOneField(to='movies.Movie')),
            ],
        ),
    ]
