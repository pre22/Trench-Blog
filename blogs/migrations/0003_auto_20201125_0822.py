# Generated by Django 3.1.3 on 2020-11-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
