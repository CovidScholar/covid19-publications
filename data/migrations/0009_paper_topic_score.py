# Generated by Django 3.0.4 on 2020-03-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20200328_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='topic_score',
            field=models.FloatField(default=0.0),
        ),
    ]
