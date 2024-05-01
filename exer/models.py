from django.db import models


class Student(models.Model):
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'




class Teacher(models.Model):
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
