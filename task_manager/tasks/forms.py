from django.forms import ModelForm
from django import forms
from task_manager.tasks.models import TaskModel
from django.contrib.auth import get_user_model

# module with texts for buttons, flash messages, titles
from task_manager import texts


User = get_user_model()


class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'title',
            'description',
            'status',
            'assignee',
            'labels',
        ]

        labels = {
            'title': texts.NAME_LABEL_FORM,
            'description': texts.DESCRIPTION_LABEL_FORM,
            'status': texts.STATUS_LABEL_FORM,
            'assignee': texts.EXECUTOR_LABEL_FORM,
            'labels': texts.LABELS_FORM,
        }

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': texts.NAME_LABEL_FORM,
                       'autofocus': 'required'}),

            'description': forms.Textarea(
                attrs={'class': 'form-control mt-2',
                       'placeholder': texts.DESCRIPTION_LABEL_FORM,
                       'style': 'height: 10em;'}),

            'status': forms.Select(attrs={'class': 'form-control mt-2'}),
            'assignee': forms.Select(attrs={'class': 'form-control mt-2'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control mt-2',
                                                  'style': 'height: 7em;'}),
        }
