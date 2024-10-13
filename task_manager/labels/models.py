from django.core.exceptions import ValidationError
from django.db import models

# module with texts for buttons, flash messages, titles
from task_manager import texts


class LabelModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.taskmodel_set.exists():
            raise ValidationError(texts.DELETE_LABEL_PROTECT_MESSAGE)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
