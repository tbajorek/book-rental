# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='book',
            field=models.ForeignKey(verbose_name='book', to='books.Book'),
        ),
    ]
