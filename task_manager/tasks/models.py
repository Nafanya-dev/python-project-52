from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import LabelModel
from django.contrib.auth import get_user_model


USER = get_user_model()


class TaskModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(USER, on_delete=models.PROTECT,
                               related_name='tasks_created')

    executor = models.ForeignKey(USER, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='tasks_assigned')

    labels = models.ManyToManyField(LabelModel,
                                    through='TaskLabelRelation',
                                    through_fields=('task', 'label'),
                                    blank=True,
                                    related_name='labels')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    label = models.ForeignKey(LabelModel, on_delete=models.PROTECT)
