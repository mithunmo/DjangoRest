# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_portalcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'ID')),
                ('portalID', models.OneToOneField(to='portal.Portal')),
                ('userID', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='portalcontent',
            name='movies',
            field=models.OneToOneField(db_column=b'movies_id', to='movies.Movie'),
        ),
    ]
