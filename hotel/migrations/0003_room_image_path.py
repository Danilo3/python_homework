# Generated by Django 2.0 on 2018-01-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20180114_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
