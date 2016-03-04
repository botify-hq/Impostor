# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpostorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('impostor_ip', models.IPAddressField(null=True, verbose_name=b"Impostor's IP address", blank=True)),
                ('logged_in', models.DateTimeField(auto_now_add=True, verbose_name=b'Logged on')),
                ('logged_out', models.DateTimeField(null=True, blank=True)),
                ('token', models.CharField(db_index=True, max_length=32, blank=True)),
                ('imposted_as', models.ForeignKey(related_name='imposted_as', verbose_name=b'Logged in as', to=settings.AUTH_USER_MODEL)),
                ('impostor', models.ForeignKey(related_name='impostor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
