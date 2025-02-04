# Generated by Django 2.2.3 on 2019-07-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0009_auto_20190723_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captureskureviewmodel',
            name='version',
        ),
        migrations.AddField(
            model_name='captureskucategoryrankmodel',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='captureskukeywordrankmodel',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='captureskubuyboxstatemodel',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='captureskucategoryrankmodel',
            name='rank_page',
            field=models.IntegerField(default=0, verbose_name='Rank Page'),
        ),
        migrations.AlterField(
            model_name='captureskukeywordrankmodel',
            name='category_title',
            field=models.CharField(max_length=100, verbose_name='Category Title'),
        ),
        migrations.AlterField(
            model_name='captureskukeywordrankmodel',
            name='rank_page',
            field=models.IntegerField(default=0, verbose_name='Rank Page'),
        ),
        migrations.AlterField(
            model_name='captureskupricemodel',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='captureskureviewmodel',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='captureskureviewmodel',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Link'),
        ),
    ]
