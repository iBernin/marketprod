# Generated by Django 5.0.1 on 2024-01-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repricer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorids',
            name='nmId',
            field=models.IntegerField(unique=True),
        ),
    ]
