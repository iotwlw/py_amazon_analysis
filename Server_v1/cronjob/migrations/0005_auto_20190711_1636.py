# Generated by Django 2.2.3 on 2019-07-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0004_auto_20190711_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronjobmodel',
            name='app_id',
        ),
        migrations.AddField(
            model_name='cronjobmodel',
            name='rule_id',
            field=models.IntegerField(null=True, verbose_name='Rule ID'),
        ),
    ]
