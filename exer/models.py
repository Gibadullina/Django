from django.db import models


class Student(models.Model):
    LEVEL_CHOICES = (
        ('bacherol', 'Бакалавр'),
        ('specialist', 'Специалист'),
        ('master', 'Магистрант')
    )

    name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=40)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)

    date_of_birth = models.DateField('Дата рождения')
    picture = models.ImageField('Фото студента', upload_to='students_pictures', null=True, blank=True)

    education_level = models.CharField('Уровень образования', max_length=100, choices=LEVEL_CHOICES,
                                       default='bacherol')
    is_budget = models.BooleanField('Бюджетник', default=False)
    ave_points = models.DecimalField('Средний балл', decimal_places=2, max_digits=2, editable=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self) -> str:
        return f'{self.last_name} {self.name}'


class Teacher(models.Model):
    POSITION_CHOICES = (
        ('senior_lecturer', 'Старший преподаватель'),
        ('assistant_professor', 'Доцент'),
        ('professor', 'Профессор')
    )

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=40)
    patronymic = models.CharField('Отчество', max_length=50, blank=True)

    date_of_birth = models.DateField('Дата рождения')
    picture = models.ImageField('Фото студента', upload_to='teacher_pictures', null=True, blank=True)

    teacher_position = models.CharField('Должность преподавателя', max_length=100, choices=POSITION_CHOICES,
                                        default='senior_lecturer')
    experience = models.PositiveIntegerField('Стаж работы', default=1)
    salary = models.DecimalField('Заработная плата', max_digits=7, decimal_places=2, editable=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
