# Generated by Django 4.2.2 on 2023-09-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='website',
        ),
    ]