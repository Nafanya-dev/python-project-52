from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status

from task_manager.mixins import AuthorizationRequiredMixin

# module with texts for buttons, flash messages, titles
from task_manager import texts


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': texts.STATUSES_LIST_TITLE_TEXT,
        'button_text': texts.CREATE_STATUS_BUTTON_TEXT
    }
