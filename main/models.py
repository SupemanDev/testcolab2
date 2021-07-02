import datetime
from django.db import models
# from django.utils import timezone


class Task(models.Model):
    title = models.CharField('Название', max_length=30)
    task = models.TextField('Описание')
    deadline = models.DateTimeField('Дедлайн', default=datetime.datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
