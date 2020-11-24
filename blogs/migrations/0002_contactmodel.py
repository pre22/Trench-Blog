# Generated by Django 3.1.3 on 2020-11-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('phone', models.IntegerField(max_length=15)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]