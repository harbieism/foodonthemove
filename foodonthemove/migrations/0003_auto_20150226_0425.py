# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodonthemove', '0002_auto_20150222_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='payment_amount',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
