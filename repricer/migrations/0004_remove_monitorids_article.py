# Generated by Django 5.0.1 on 2024-01-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repricer', '0003_monitorids_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitorids',
            name='article',
        ),
    ]
