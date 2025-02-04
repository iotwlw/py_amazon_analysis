# Generated by Django 2.2 on 2019-07-22 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfront', '0007_auto_20190722_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productasinmodel',
            name='category',
        ),
        migrations.CreateModel(
            name='ProductCategoryRelationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('purchase_product_id', models.CharField(max_length=200, null=True, verbose_name='Purchase Product Id')),
                ('purchase_category_id', models.CharField(max_length=200, null=True, verbose_name='Purchase Product Id')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appfront.ProductCategoryModel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appfront.ProductAsinModel')),
            ],
            options={
                'db_table': 'pub_product_asin_category_relation',
            },
        ),
    ]
