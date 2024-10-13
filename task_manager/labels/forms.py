from django.forms import ModelForm
from django import forms
from task_manager.labels.models import LabelModel

# module with texts for buttons, flash messages, titles
from task_manager import texts


class LabelForm(ModelForm):
    name = forms.CharField(label=texts.NAME_LABEL_FORM,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': texts.NAME_LABEL_FORM,
                                      'autofocus': 'required'}))

    class Meta:
        model = LabelModel
        fields = ['name']