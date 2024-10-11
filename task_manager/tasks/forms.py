from django.forms import ModelForm
from django import forms
from task_manager.tasks.models import TaskModel


class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'title',
            'description',
            'status',
            'assignee',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Name',
                                            'autofocus': 'required'}),

            'description': forms.Textarea(attrs={'class': 'form-control mt-2',
                                                 'placeholder': 'description',
                                                 'style': 'height: 10em;'}),

            'status': forms.Select(attrs={'class': 'form-control mt-2'}),
            'assignee': forms.Select(attrs={'class': 'form-control mt-2'})
        }
