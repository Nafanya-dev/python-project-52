from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm

from task_manager.mixins import AuthorizationRequiredMixin

# module with texts for buttons, flash messages, titles
from task_manager import texts


class StatusListView(AuthorizationRequiredMixin, ListView):
    """
    URL ('/statuses/')
    Method GET Returns the HTML code of the status list page.
    """
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': texts.STATUSES_LIST_TITLE_TEXT,
        'button_text': texts.CREATE_STATUS_TEXT
    }

    authorization_message = texts.AUTHORIZATION_MESSAGE


class CreateStatusView(AuthorizationRequiredMixin, SuccessMessageMixin,
                       CreateView):
    """
    URL ('/statuses/create/')

    Method GET Returns the HTML code of the creating status.
    Method POST Creates a new status and redirects
    to the status list page ('/statuses/')
    """
    form_class = StatusForm
    template_name = 'statuses/update_create_status_form.html'
    success_url = reverse_lazy('status-list-page')
    extra_context = {
        'title': texts.CREATE_STATUS_TEXT,
        'button_text': texts.CREATE_BUTTON_TEXT
    }

    success_message = texts.CREATE_STATUS_SUCCESS_MESSAGE
    authorization_message = texts.AUTHORIZATION_MESSAGE


class UpdateStatusView(AuthorizationRequiredMixin, SuccessMessageMixin,
                       UpdateView):
    """
    URL ('/statuses/<pk>/update/').

    Method GET Returns the HTML code of form with status data for editing
    Method POST Updates status and redirects to
    the status list page ('/statuses/')
    """
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update_create_status_form.html'
    success_url = reverse_lazy('status-list-page')
    extra_context = {
        'title': texts.UPDATE_STATUS_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    success_message = texts.UPDATE_STATUS_SUCCESS_MESSAGE
    authorization_message = texts.AUTHORIZATION_MESSAGE


class DeleteStatusView(AuthorizationRequiredMixin, SuccessMessageMixin,
                       DeleteView):
    """
    URL ('/statuses/<pk>/delete/').

    Method GET Returns the HTML code of the status deletion confirmation page
    Method POST delete status and redirects to the status list page
    """
    model = Status
    template_name = 'statuses/delete_status.html'
    context_object_name = 'status'
    success_url = reverse_lazy('status-list-page')
    extra_context = {
        'title': texts.DELETE_STATUS_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT
    }

    success_message = texts.DELETE_STATUS_SUCCESS_MESSAGE
    authorization_message = texts.AUTHORIZATION_MESSAGE
