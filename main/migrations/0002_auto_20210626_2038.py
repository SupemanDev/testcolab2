# Generated by Django 3.2.4 on 2021-06-26 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 26, 17, 38, 2, 716346, tzinfo=utc), verbose_name='Дедлайн'),
        ),
    ]
