from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import TaskModel
from task_manager.labels.models import LabelModel
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from django import forms

# module containing the texts of common buttons and form titles
from task_manager import texts


USER = get_user_model()

SELF_TASKS_LABEL_FORM = _('Only own tasks')


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        label=texts.STATUS_LABEL_FORM,
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control is-valid mt-2'}),
    )

    executor = ModelChoiceFilter(
        label=texts.EXECUTOR_LABEL_FORM,
        queryset=USER.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control is-valid mt-2'}),
    )

    label = ModelChoiceFilter(
        label=texts.LABEL_FORM,
        queryset=LabelModel.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control is-valid mt-2'}),
        field_name='labels',
    )

    self_tasks = BooleanFilter(
        label=SELF_TASKS_LABEL_FORM,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input mt-2'}),
        method='get_own_tasks',
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = TaskModel

        fields = ['status', 'executor', 'label']
