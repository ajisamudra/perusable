# Generated by ajisamudra on 2022-20-17 11:42

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_wine_thumbnail"),
    ]

    operations = [
        TrigramExtension(),
    ]
