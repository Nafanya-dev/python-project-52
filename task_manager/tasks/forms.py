from django.forms import ModelForm
from django import forms
from task_manager.tasks.models import TaskModel
from django.contrib.auth import get_user_model

# module that stores all texts for the project in one place,
# buttons, headings, messages
from task_manager import texts


User = get_user_model()


class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]

        labels = {
            'name': texts.NAME_LABEL_FORM,
            'description': texts.DESCRIPTION_LABEL_FORM,
            'status': texts.STATUS_LABEL_FORM,
            'executor': texts.EXECUTOR_LABEL_FORM,
            'labels': texts.LABELS_FORM,
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': texts.NAME_LABEL_FORM,
                       'autofocus': 'required'}),

            'description': forms.Textarea(
                attrs={'class': 'form-control mt-2',
                       'placeholder': texts.DESCRIPTION_LABEL_FORM,
                       'style': 'height: 10em;'}),

            'status': forms.Select(attrs={'class': 'form-control mt-2'}),
            'executor': forms.Select(attrs={'class': 'form-control mt-2'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control mt-2',
                                                  'style': 'height: 7em;'}),
        }
