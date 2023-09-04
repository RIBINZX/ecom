# Generated by Django 4.2.2 on 2023-09-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_review_email_remove_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
