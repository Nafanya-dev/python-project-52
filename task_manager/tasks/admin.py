from django.contrib import admin
from task_manager.tasks.models import TaskModel


admin.site.register(TaskModel)
