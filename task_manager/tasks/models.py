from django.db import models

from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


User = get_user_model()

class TaskModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='tasks_created')

    assignee = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='tasks_assigned')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
