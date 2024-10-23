from task_manager.tasks.tests.task_test_case import TaskTestCase
from task_manager.tasks.tests.filter_tasks_test_case import FilterTaskTestCase
from task_manager.tasks.models import TaskModel


class CreateTaskViewTest(TaskTestCase):
    def test_create_task_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('create_url'))
        self.assertRedirects(response,
                             self.get_urls().get('login_url'))

    def test_create_task_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('create_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_create_task(self):
        self.client.force_login(self.user)

        self.assertEqual(TaskModel.objects.count(), 1)
        response = self.client.post(self.get_urls().get('create_url'),
                                    self.get_data().get('Create_data'))

        self.assertRedirects(response, self.get_urls().get('task_list_url'))
        self.assertEqual(TaskModel.objects.count(), 2)
        self.assertTrue(TaskModel.objects.filter(name='New Task').exists())


class UpdateTaskViewTest(TaskTestCase):
    def test_update_task_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('update_url'))
        self.assertRedirects(response, self.get_urls().get('login_url'))

    def test_update_task_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('update_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_update_task(self):
        self.client.force_login(self.user)

        response = self.client.post(self.get_urls().get('update_url'),
                                    self.get_data().get('Updated_data'))

        self.assertRedirects(response, self.get_urls().get('task_list_url'))

        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')


class DeleteTaskViewTest(TaskTestCase):
    def test_delete_task_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('delete_url'))
        self.assertRedirects(response, self.get_urls().get('login_url'))

    def test_delete_task_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('delete_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('delete'))

    def test_delete_task_wrong_user(self):
        self.client.force_login(self.wrong_user)

        response = self.client.post(self.get_urls().get('delete_url'))
        self.assertTrue(TaskModel.objects.filter(pk=self.task.pk).exists())
        self.assertRedirects(response, self.get_urls().get('task_list_url'))

    def test_delete_task(self):
        self.client.force_login(self.user)

        self.assertEqual(TaskModel.objects.count(), 1)
        response = self.client.post(self.get_urls().get('delete_url'))
        self.assertEqual(TaskModel.objects.count(), 0)
        self.assertFalse(TaskModel.objects.filter(pk=self.task.pk).exists())
        self.assertRedirects(response, self.get_urls().get('task_list_url'))


class FilterTaskTest(FilterTaskTestCase):
    def test_filter_by_status(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('task_list_url'),
                                   {'status': self.status1.id})

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.task1, response.context['tasks'])
        self.assertIn(self.task3, response.context['tasks'])
        self.assertNotIn(self.task2, response.context['tasks'])

    def test_filter_by_label(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('task_list_url'),
                                   {'label': self.label1.id})

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.task2, response.context['tasks'])
        self.assertNotIn(self.task1, response.context['tasks'])
        self.assertNotIn(self.task3, response.context['tasks'])

    def test_filter_self_tasks(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('task_list_url'),
                                   {'self_tasks': 'on'})

        self.assertEqual(response.status_code, 200)
        for task in response.context['tasks']:
            self.assertEqual(task.author, self.user)
