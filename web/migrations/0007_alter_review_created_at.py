# Generated by Django 4.2.2 on 2023-09-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_review_email_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]