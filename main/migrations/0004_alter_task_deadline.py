# Generated by Django 3.2.4 on 2021-06-26 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 26, 17, 47, 28, 249536, tzinfo=utc), verbose_name='Дедлайн'),
        ),
    ]
