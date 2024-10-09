from django.forms import ModelForm
from django import forms
from task_manager.statuses.models import Status

# module with texts for buttons, flash messages, titles
from task_manager import texts


class StatusForm(ModelForm):
    name = forms.CharField(label=texts.NAME_LABEL_STATUS_FORM)

    class Meta:
        model = Status
        fields = ['name']
