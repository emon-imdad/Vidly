# Generated by Django 4.1.7 on 2023-02-23 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 12, 43, 1, 262983, tzinfo=datetime.timezone.utc)),
        ),
    ]
