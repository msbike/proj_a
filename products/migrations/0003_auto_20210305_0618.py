# Generated by Django 3.1.7 on 2021-03-05 05:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210305_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='validfrom',
        ),
        migrations.AddField(
            model_name='product',
            name='valid_from',
            field=models.DateField(default=datetime.datetime(2021, 3, 5, 5, 18, 38, 453697, tzinfo=utc)),
        ),
    ]
