from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import TaskModel
from django.contrib.auth import get_user_model

# module containing the texts of common buttons and form titles
from task_manager import texts


User = get_user_model()

DESCRIPTION_LABEL_FORM = _('Description')
LABELS_FORM = _('Labels')


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
            'description': DESCRIPTION_LABEL_FORM,
            'status': texts.STATUS_LABEL_FORM,
            'executor': texts.EXECUTOR_LABEL_FORM,
            'labels': LABELS_FORM,
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': texts.NAME_LABEL_FORM,
                       'autofocus': 'required'}),

            'description': forms.Textarea(
                attrs={'class': 'form-control mt-2',
                       'placeholder': DESCRIPTION_LABEL_FORM,
                       'style': 'height: 10em;'}),

            'status': forms.Select(attrs={'class': 'form-control mt-2'}),
            'executor': forms.Select(attrs={'class': 'form-control mt-2'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control mt-2',
                                                  'style': 'height: 7em;'}),
        }
