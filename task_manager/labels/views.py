from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import LabelModel
from task_manager.labels.forms import LabelForm
from task_manager.mixins import (AuthorizationRequiredMixin,
                                 DeleteProtectionMixin)

# module with texts for buttons, flash messages, titles
from task_manager import texts


LABEL_LIST_URL = reverse_lazy('label-list-page')

UPDATE_CREATE_TEMPLATE = 'update_create_form.html'


class LabelListView(AuthorizationRequiredMixin, ListView):
    """
    URL ('/labels/')

    Method GET Returns the HTML code of the label list page.
    """
    model = LabelModel
    template_name = 'status_label_list.html'
    context_object_name = 'objects'
    extra_context = {
        'title': texts.LABEL_LIST_TITLE_TEXT,
        'button_text': texts.CREATE_LABEL_TEXT,
        'create_url': 'create-label-page',
        'update_url': 'update-label-page',
        'delete_url': 'delete-label-page'
    }


class CreateLabelView(AuthorizationRequiredMixin, SuccessMessageMixin,
                      CreateView):
    """
    URL ('/labels/create/')

    Method GET Returns the HTML code of the creating label.
    Method POST Creates a new label and redirects
    to the label list page ('/labels/')
    """
    form_class = LabelForm
    template_name = UPDATE_CREATE_TEMPLATE
    extra_context = {
        'title': texts.CREATE_LABEL_TEXT,
        'button_text': texts.CREATE_BUTTON_TEXT
    }

    success_url = LABEL_LIST_URL

    success_message = texts.CREATE_LABEL_SUCCESS_MESSAGE


class UpdateLabelView(AuthorizationRequiredMixin, SuccessMessageMixin,
                      UpdateView):
    """
    URL ('/labels/<pk>/update/').

    Method GET Returns the HTML code of form with label data for editing
    Method POST Updates label and redirects to
    the label list page ('/labels/')
    """
    model = LabelModel
    form_class = LabelForm
    template_name = UPDATE_CREATE_TEMPLATE
    extra_context = {
        'title': texts.UPDATE_LABEL_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    success_url = LABEL_LIST_URL

    success_message = texts.UPDATE_LABEL_SUCCESS_MESSAGE


class DeleteLabelView(AuthorizationRequiredMixin, DeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):
    """
    URL ('/labels/<pk>/delete/').

    Method GET Returns the HTML code of the label deletion confirmation page.
    Method POST delete label and redirects to the label list page
    """
    model = LabelModel
    template_name = 'delete_form.html'
    context_object_name = 'object'
    extra_context = {
        'title': texts.DELETE_LABEL_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT
    }

    success_url = LABEL_LIST_URL
    protected_url = LABEL_LIST_URL

    success_message = texts.DELETE_LABEL_SUCCESS_MESSAGE
    protected_message = texts.DELETE_LABEL_PROTECT_MESSAGE
