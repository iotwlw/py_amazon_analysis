# Generated by Django 2.2.3 on 2019-07-24 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0004_auto_20190716_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisrulemodel',
            name='capture_rule',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='rule.CaptureRuleModel', verbose_name='Capture Rule'),
        ),
        migrations.AddField(
            model_name='analysisrulemodel',
            name='xml_data',
            field=models.TextField(max_length=10000, null=True, verbose_name='Xml Data'),
        ),
        migrations.AlterField(
            model_name='analysisrulemodel',
            name='description',
            field=models.TextField(max_length=10000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='captureruleurlmodel',
            name='params',
            field=models.TextField(default='', null=True, verbose_name='Url Params'),
        ),
        migrations.AlterField(
            model_name='captureruleurlmodel',
            name='path',
            field=models.TextField(default='', null=True, verbose_name='Path Params'),
        ),
    ]
