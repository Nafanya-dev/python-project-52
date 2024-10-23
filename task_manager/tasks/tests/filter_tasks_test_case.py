from task_manager.tests.base_test_case import BaseTestCase
from django.urls import reverse_lazy

from task_manager.statuses.models import Status
from task_manager.tasks.models import TaskModel
from task_manager.labels.models import LabelModel


class FilterTaskTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.status1 = Status.objects.create(name='Open')
        self.status2 = Status.objects.create(name='Closed')

        self.label1 = LabelModel.objects.create(name='Important')
        self.label2 = LabelModel.objects.create(name='Urgent')

        self.task1 = TaskModel.objects.create(name='Task 1',
                                              status=self.status1,
                                              author=self.user)

        self.task2 = TaskModel.objects.create(name='Task 2',
                                              status=self.status2,
                                              author=self.user)
        self.task2.labels.add(self.label1)

        self.task3 = TaskModel.objects.create(name='Task 3',
                                              status=self.status1,
                                              author=self.user)
        self.task3.labels.add(self.label2)

    def get_urls(self):
        return {
            'task_list_url': reverse_lazy('task-list-page'),
        }
