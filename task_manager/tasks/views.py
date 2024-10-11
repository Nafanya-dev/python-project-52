from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from task_manager.tasks.models import TaskModel
from task_manager.tasks.forms import TaskForm

# module with texts for buttons, flash messages, titles
from task_manager import texts


class TaskListView(ListView):
    model = TaskModel
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': texts.TASKS_LIST_TITLE_TEXT,
        'button_text': texts.CREATE_TASK_TEXT
    }


class CreateTaskView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/update_create_task_form.html'
    success_url = reverse_lazy('task-list-page')
    extra_context = {
        'title': texts.CREATE_TASK_TEXT,
        'button_text': texts.CREATE_BUTTON_TEXT
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
