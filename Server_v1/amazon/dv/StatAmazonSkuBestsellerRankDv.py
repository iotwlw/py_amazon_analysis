# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


'''按关键词统计的每天视图数据'''
class StatAmazonSkuBestsellerRankDayDv(models.Model):
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    category_id = models.IntegerField(verbose_name=_('Category Id'))
    dy = models.DateField(verbose_name=_('Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "amazon"
        managed = False
        db_table = 'view_i_amazon_sku_bestseller_rank_day'
        verbose_name_plural = _('Keyword Rank for days')


'''按关键词统计的每月视图数据'''
class StatAmazonSkuBestsellerRankMonthDv(models.Model):
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    category_id = models.IntegerField(verbose_name=_('Category Id'))
    yr = models.IntegerField(verbose_name=_('Year'), null=True)
    mo = models.IntegerField(verbose_name=_('Month'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "amazon"
        managed = False
        db_table = 'view_i_amazon_sku_bestseller_rank_month'
        verbose_name_plural = _('Keyword Rank for months')


'''按关键词统计的每周视图数据'''
class StatAmazonSkuBestsellerRankWeekDv(models.Model):
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    category_id = models.IntegerField(verbose_name=_('Category Id'))
    yr = models.IntegerField(verbose_name=_('Year'), null=True)
    wk = models.IntegerField(verbose_name=_('Week'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "amazon"
        managed = False
        db_table = 'view_i_amazon_sku_bestseller_rank_week'
        verbose_name_plural = _('Keyword Rank for weeks')
