# Generated by Django 2.0.7 on 2018-07-14 14:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180714_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copy',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('ca25ae90-8773-11e8-8788-dc85de5badef'), primary_key=True, serialize=False),
        ),
    ]
