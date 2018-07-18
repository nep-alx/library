# Generated by Django 2.0.7 on 2018-07-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Degree',
        ),
        migrations.AddField(
            model_name='author',
            name='degree',
            field=models.IntegerField(choices=[(0, 'Нет'), (1, 'Бакалавр'), (2, 'Магистр'), (3, 'Кандидат технических наук'), (4, 'Доктор технических наук')], default=0, verbose_name='Научная степень'),
        ),
    ]
