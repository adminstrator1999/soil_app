# Generated by Django 3.2.5 on 2021-07-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]