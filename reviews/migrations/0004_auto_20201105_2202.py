# Generated by Django 3.0.6 on 2020-11-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20201105_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='book_thumbnails'),
        ),
    ]
