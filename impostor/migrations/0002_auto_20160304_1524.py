# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impostor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impostorlog',
            name='impostor_ip',
            field=models.GenericIPAddressField(null=True, verbose_name=b"Impostor's IP address", blank=True),
        ),
    ]
