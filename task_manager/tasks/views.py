from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView, DetailView)

from task_manager.mixins import (AuthorizationRequiredMixin,
                                 AuthorDeletionMixin)

from task_manager.tasks.models import TaskModel
from task_manager.tasks.forms import TaskForm

# module with texts for buttons, flash messages, titles
from task_manager import texts


TASK_LIST_URL = reverse_lazy('task-list-page')

UPDATE_CREATE_TEMPLATE = 'update_create_form.html'

class TaskListView(AuthorizationRequiredMixin, ListView):
    """
    URL ('/tasks/')

    Method GET Returns the HTML code of the task list page.
    """
    model = TaskModel
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': texts.TASKS_LIST_TITLE_TEXT,
        'button_text': texts.CREATE_TASK_TEXT
    }


class TaskDetailView(AuthorizationRequiredMixin, DetailView):
    """
    URL ('/tasks/<pk>/'

    Method GET Returns HTML task details
    """
    model = TaskModel
    template_name = 'tasks/detail_task.html'
    context_object_name = 'task'
    extra_context = {
        'title': texts.DETAIL_TASK_TITLE_TEXT
    }


class CreateTaskView(AuthorizationRequiredMixin, SuccessMessageMixin,
                     CreateView):
    """
    URL ('/tasks/create/')

    Method GET Returns the HTML code of the creating task.
    Method POST Creates a new task and redirects
    to the task list page ('/tasks/')
    """
    form_class = TaskForm
    template_name = UPDATE_CREATE_TEMPLATE
    extra_context = {
        'title': texts.CREATE_TASK_TEXT,
        'button_text': texts.CREATE_BUTTON_TEXT
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = TASK_LIST_URL

    success_message = texts.CREATE_TASK_SUCCESS_MESSAGE


class UpdateTaskView(AuthorizationRequiredMixin,SuccessMessageMixin,
                     UpdateView):
    """
    URL ('/tasks/<pk>/update/').

    Method GET Returns the HTML code of form with task data for editing
    Method POST Updates task and redirects to
    the task list page ('/tasks/')
    """
    model = TaskModel
    form_class = TaskForm
    template_name = UPDATE_CREATE_TEMPLATE
    extra_context = {
        'title': texts.UPDATE_TASK_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    success_url = TASK_LIST_URL

    success_message = texts.UPDATE_TASK_SUCCESS_MESSAGE


class DeleteTaskView(AuthorizationRequiredMixin, AuthorDeletionMixin,
                     SuccessMessageMixin, DeleteView):
    """
    URL ('/tasks/<pk>/delete/').

    Method GET Returns the HTML code of the task deletion confirmation page.
    Method POST delete task and redirects to the task list page
    """
    model = TaskModel
    template_name = 'delete_form.html'
    context_object_name = 'object'
    extra_context = {
        'title': texts.DELETE_TASK_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT
    }

    success_url = TASK_LIST_URL
    author_redirect_url = TASK_LIST_URL

    success_message = texts.DELETE_TASK_SUCCESS_MESSAGE
    author_message = texts.AUTHOR_TASK_MESSAGE
