from django.db import models


class Student(models.Model):
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self) -> str:
        return self.name



class Teacher(models.Model):
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
    def __str__(self) -> str:
        return self.name