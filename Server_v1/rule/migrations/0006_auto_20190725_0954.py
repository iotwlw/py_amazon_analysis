# Generated by Django 2.2.3 on 2019-07-25 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0005_auto_20190724_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturerulemodel',
            name='xml_data',
            field=models.TextField(max_length=10000, null=True, verbose_name='Xml Data'),
        ),
        migrations.AlterField(
            model_name='analysisrulemodel',
            name='capture_rule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rule.CaptureRuleModel', verbose_name='Capture Rule'),
        ),
    ]
