# Generated by Django 2.2 on 2019-07-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0003_auto_20190710_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjobmodel',
            name='task_type',
            field=models.IntegerField(choices=[(1, 'Capture'), (2, 'Transformation'), (3, 'Analysis'), (4, 'Message'), (5, 'Report'), (9, 'Other')], default=1, verbose_name='Task Type'),
        ),
    ]
