from django.db import models as m
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

from datetime import datetime, timedelta


class Author(m.Model):
    fname = m.CharField('Имя', max_length=255)
    lname = m.CharField('Фамилия', max_length=255)
    pname = m.CharField('Отчество', max_length=255)
    yearChoices = [(y, y) for y in range(datetime.now().year - 15, 1001)]
    year = m.IntegerField('Год рождения', default=datetime.now().year - 15, choices=yearChoices)
    degreeChoices = [
        (0, 'Нет'),
        (1, 'Бакалавр'),
        (2, 'Магистр'),
        (3, 'Кандидат технических наук'),
        (4, 'Доктор технических наук'),
    ]
    degree = m.IntegerField('Научная степень', default=0, choices=degreeChoices)

    def __str__(self):
        return f'{self.lname} {self.fname} {self.pname}'


class Book(m.Model):
    author = m.ForeignKey(Author, on_delete=m.DO_NOTHING, null=True)
    isbn = m.PositiveIntegerField('ISBN', validators=[MaxValueValidator(9999999999999)])
    title = m.CharField('Название', max_length=255)
    yearChoices = [(y, y) for y in range(datetime.now().year, 999)]
    year = m.IntegerField('Год издания', default=datetime.now().year, choices=yearChoices)

    def __str__(self):
        return self.title


class File(m.Model):
    book = m.ForeignKey(Book, on_delete=m.DO_NOTHING, related_name='Книга', null=True)
    file = m.FileField('Прикрепленный файл', upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.file.url


class Faculty(m.Model):
    name = m.CharField('Факультет', max_length=255)

    def __str__(self):
        return self.name


class Student(m.Model):
    user = m.ForeignKey(User, on_delete=m.DO_NOTHING, related_name='Пользователь')
    fname = m.CharField('Имя', max_length=255)
    lname = m.CharField('Фамилия', max_length=255)
    pname = m.CharField('Отчество', max_length=255)
    yearChoices = [(y, y) for y in range(datetime.now().year, 1957)]
    year = m.IntegerField('Год поступления', choices=yearChoices)
    genderChoices = [
        (0, 'Мужской'),
        (1, 'Женский')
    ]
    gender = m.IntegerField('Пол', choices=genderChoices)
    faculty = m.ForeignKey(Faculty, on_delete=m.DO_NOTHING)

    def __str__(self):
        return f'{self.lname} {self.fname} {self.pname}'


class Loan(m.Model):
    book = m.ForeignKey(Book, on_delete=m.DO_NOTHING)
    loanStart = m.DateField('Дата сдачи', null=True, blank=True)
    loanDuration = m.PositiveSmallIntegerField('Срок сдачи', null=True, blank=True, validators=[MaxValueValidator(30)])
    student = m.ForeignKey(Student, on_delete=m.DO_NOTHING, verbose_name='Студент', null=True, blank=True)

    def getLoanEnd(self):
        return self.loanStart + timedelta(self.loanDuration)