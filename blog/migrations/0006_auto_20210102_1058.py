# Generated by Django 3.1.4 on 2021-01-02 05:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210102_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 5, 28, 12, 949870, tzinfo=utc)),
        ),
    ]
