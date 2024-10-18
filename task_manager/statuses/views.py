from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.utils.enums import Template
from task_manager.mixins import (AuthorizationRequiredMixin,
                                 DeleteProtectionMixin)

from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm

# module containing the texts of common buttons and form titles
from task_manager import texts


STATUS_LIST_URL = reverse_lazy('status-list-page')

CREATE_STATUS_TEXT = _('Create Status')
CREATE_STATUS_SUCCESS_MESSAGE = _('Status successfully created')
UPDATE_STATUS_SUCCESS_MESSAGE = _('Status successfully changed')
DELETE_STATUS_SUCCESS_MESSAGE = _('Status successfully deleted')
DELETE_STATUS_PROTECT_MESSAGE = _('Cannot delete status because it is in use')


STATUSES_LIST_TITLE_TEXT = _('Statuses')
UPDATE_STATUS_TITLE_TEXT = _('Change Status')
DELETE_STATUS_TITLE_TEXT = _('Delete status')


class StatusListView(AuthorizationRequiredMixin, ListView):
    """
    URL ('/statuses/')

    Method GET Returns the HTML code of the status list page.
    """
    model = Status
    template_name = 'status_label_list.html'
    context_object_name = 'objects'
    extra_context = {
        'title': STATUSES_LIST_TITLE_TEXT,
        'button_text': CREATE_STATUS_TEXT,
        'create_url': 'create-status-page',
        'update_url': 'update-status-page',
        'delete_url': 'delete-status-page'
    }


class CreateStatusView(AuthorizationRequiredMixin, SuccessMessageMixin,
                       CreateView):
    """
    URL ('/statuses/create/')

    Method GET Returns the HTML code of the creating status.
    Method POST Creates a new status and redirects
    to the status list page ('/statuses/')
    """
    form_class = StatusForm
    template_name = Template.update_create.value
    extra_context = {
        'title': CREATE_STATUS_TEXT,
        'button_text': texts.CREATE_BUTTON_TEXT
    }

    success_url = STATUS_LIST_URL

    success_message = CREATE_STATUS_SUCCESS_MESSAGE


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
    template_name = Template.update_create.value
    extra_context = {
        'title': UPDATE_STATUS_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    success_url = STATUS_LIST_URL

    success_message = UPDATE_STATUS_SUCCESS_MESSAGE


class DeleteStatusView(AuthorizationRequiredMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):
    """
    URL ('/statuses/<pk>/delete/').

    Method GET Returns the HTML code of the status deletion confirmation page
    Method POST delete status and redirects to the status list page
    """
    model = Status
    template_name = Template.delete.value
    context_object_name = 'object'
    extra_context = {
        'title': DELETE_STATUS_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT
    }

    success_url = STATUS_LIST_URL
    protected_url = STATUS_LIST_URL

    protected_message = DELETE_STATUS_PROTECT_MESSAGE
    success_message = DELETE_STATUS_SUCCESS_MESSAGE
