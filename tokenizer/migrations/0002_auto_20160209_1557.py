# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokenizer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='encoded_text',
        ),
        migrations.AddField(
            model_name='question',
            name='volunteer',
            field=models.CharField(default=b'Kamini', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
