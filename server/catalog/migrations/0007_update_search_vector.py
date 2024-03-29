# Generated by Django 3.2.9 on 2022-06-22 15:09

from django.contrib.postgres.search import SearchVector
from django.db import migrations


def update_search_vector(apps, schema_editor):
    Wine = apps.get_model("catalog", "Wine")
    Wine.objects.all().update(
        search_vector=(
            SearchVector("variety", weight="A")
            + SearchVector("winery", weight="A")
            + SearchVector("description", weight="B")
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_search_vector"),
    ]

    operations = [migrations.RunPython(update_search_vector, elidable=True)]
