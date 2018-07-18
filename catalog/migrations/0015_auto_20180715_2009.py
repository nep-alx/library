# Generated by Django 2.0.7 on 2018-07-15 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20180715_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copy',
            name='book',
        ),
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Book'),
        ),
        migrations.DeleteModel(
            name='Copy',
        ),
    ]