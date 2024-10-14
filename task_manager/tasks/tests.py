from task_manager.fixtures.task_test_case import TaskTestCase
from task_manager.tasks.models import TaskModel


class CreateTaskViewTest(TaskTestCase):
    def test_create_task_view_without_authentication(self):
        response = self.client.get(self.urls.get('create_url'))
        self.assertRedirects(response,
                             self.urls.get('login_url'))

    def test_create_task_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('create_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_create_task(self):
        self.client.force_login(self.user)

        response = self.client.post(self.urls.get('create_url'),
                                    self.data.get('Create_data'))

        self.assertRedirects(response, self.urls.get('task_list_url'))
        self.assertTrue(TaskModel.objects.filter(name='New Task').exists())


class UpdateTaskViewTest(TaskTestCase):
    def test_update_task_view_without_authentication(self):
        response = self.client.get(self.urls.get('update_url'))
        self.assertRedirects(response, self.urls.get('login_url'))

    def test_update_task_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('update_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_update_task(self):
        self.client.force_login(self.user)

        response = self.client.post(self.urls.get('update_url'),
                                    self.data.get('Updated_data'))

        self.assertRedirects(response, self.urls.get('task_list_url'))

        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')


class DeleteTaskViewTest(TaskTestCase):
    def test_delete_task_view_without_authentication(self):
        response = self.client.get(self.urls.get('delete_url'))
        self.assertRedirects(response, self.urls.get('login_url'))

    def test_delete_task_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('delete_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('delete'))

    def test_delete_task_wrong_user(self):
        self.client.force_login(self.wrong_user)

        response = self.client.post(self.urls.get('delete_url'))
        self.assertTrue(TaskModel.objects.filter(pk=self.task.pk).exists())
        self.assertRedirects(response, self.urls.get('task_list_url'))

    def test_delete_task(self):
        self.client.force_login(self.user)

        response = self.client.post(self.urls.get('delete_url'))
        self.assertFalse(TaskModel.objects.filter(pk=self.task.pk).exists())
        self.assertRedirects(response, self.urls.get('task_list_url'))
