# Generated by Django 2.0.7 on 2018-07-14 14:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180714_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='id',
            field=models.UUIDField(default=uuid.UUID('01183f87-fc50-4465-9366-0703a59a1357'), primary_key=True, serialize=False),
        ),
    ]
