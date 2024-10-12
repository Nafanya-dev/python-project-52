from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthorizationRequiredMixin, AuthorDeletionMixin

from task_manager.tasks.models import TaskModel
from task_manager.tasks.forms import TaskForm

# module with texts for buttons, flash messages, titles
from task_manager import texts


class TaskListView(AuthorizationRequiredMixin, ListView):
    model = TaskModel
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': texts.TASKS_LIST_TITLE_TEXT,
        'button_text': texts.CREATE_TASK_TEXT
    }


class TaskDetailView(AuthorizationRequiredMixin, DetailView):
    model = TaskModel
    template_name = 'tasks/detail_task.html'
    context_object_name = 'task'
    extra_context = {
        'title': texts.DETAIL_TASK_TITLE_TEXT
    }


class CreateTaskView(AuthorizationRequiredMixin, SuccessMessageMixin,
                     CreateView):
    form_class = TaskForm
    template_name = 'update_create_form.html'
    success_url = reverse_lazy('task-list-page')
    extra_context = {
        'title': texts.CREATE_TASK_TEXT,
        'button_text': texts.CREATE_BUTTON_TEXT
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_message = texts.CREATE_TASK_SUCCESS_MESSAGE


class UpdateTaskView(AuthorizationRequiredMixin,SuccessMessageMixin,
                     UpdateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'update_create_form.html'
    success_url = reverse_lazy('task-list-page')
    extra_context = {
        'title': texts.UPDATE_TASK_TITLE_TEXT,
        'button_text': texts.EDIT_BUTTON_TEXT
    }

    success_message = texts.UPDATE_TASK_SUCCESS_MESSAGE


class DeleteTaskView(AuthorizationRequiredMixin, AuthorDeletionMixin,
                     SuccessMessageMixin, DeleteView):
    model = TaskModel
    template_name = 'delete_form.html'
    context_object_name = 'object'
    success_url = reverse_lazy('task-list-page')
    author_url = reverse_lazy('task-list-page')
    extra_context = {
        'title': texts.DELETE_TASK_TITLE_TEXT,
        'button_text': texts.DELETE_BUTTON_TEXT
    }

    success_message = texts.DELETE_TASK_SUCCESS_MESSAGE
    author_message = texts.AUTHOR_TASK_MESSAGE
