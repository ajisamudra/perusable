# Generated by Django 3.2.9 on 2022-06-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='wines'),
        ),
    ]
