# Generated by Django 2.2 on 2019-08-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0014_auto_20190805_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amazonproductcategorykeywordrelation',
            old_name='amazon_category_id',
            new_name='amazon_category',
        ),
        migrations.RenameField(
            model_name='amazonproductcategorykeywordrelation',
            old_name='amazon_keyword_id',
            new_name='amazon_keyword',
        ),
    ]
