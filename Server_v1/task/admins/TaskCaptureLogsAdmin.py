# coding:utf-8
from task.forms import TaskCaptureLogsForm
from task.model import *
from django.contrib import admin
from cronjob.admins import CronjobLogsAdmin

from django.utils.translation import ugettext as _


@admin.register(TaskCaptureLogsModel)
class TaskCaptureLogsAdmin(CronjobLogsAdmin):
    list_display = ('cronjob', 'colored_status', 'task_type', 'process', 'thread', 'date_begin', 'date_end', 'time_long', 'created_at')
    list_filter = ('status',)
    form = TaskCaptureLogsForm

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False
