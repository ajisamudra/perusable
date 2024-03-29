# Generated by Django 3.2.9 on 2022-06-20 04:58

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_install_trigram_ext'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='wine',
            index=django.contrib.postgres.indexes.GinIndex(fields=['variety', 'winery', 'description'], name='gin_idx', opclasses=['gin_trgm_ops', 'gin_trgm_ops', 'gin_trgm_ops']),
        ),
    ]
