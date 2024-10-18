from django.forms import ModelForm
from django import forms
from task_manager.statuses.models import Status

# module containing the texts of common buttons and form titles
from task_manager import texts


class StatusForm(ModelForm):
    name = forms.CharField(label=texts.NAME_LABEL_FORM,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': texts.NAME_LABEL_FORM,
                                      'autofocus': 'required'}))

    class Meta:
        model = Status
        fields = ['name']
