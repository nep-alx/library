# Generated by Django 2.0.7 on 2018-07-14 14:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180714_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3462687a-462e-4db0-ba67-2895277b6925'), editable=False, primary_key=True, serialize=False),
        ),
    ]
