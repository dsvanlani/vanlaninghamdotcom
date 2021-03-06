# Generated by Django 3.0.6 on 2020-11-06 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20201105_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commenterEmail',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
