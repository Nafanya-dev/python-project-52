from task_manager.tasks.models import TaskModel


class CreateStatusViewTest(StatusTestCase):
    def test_create_status_view_without_authentication(self):
        response = self.client.get(self.create_url)
        self.assertRedirects(response,
                             self.login_url)

    def test_create_status_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.update_create_template)

    def test_status_creation(self):
        self.client.force_login(self.user)
        self.assertEqual(TaskModel.objects.count(), 1)

        response = self.client.post(self.create_url, self.create_data)
        self.assertRedirects(response, self.status_list_url)
        self.assertEqual(TaskModel.objects.count(), 2)

        task = TaskModel.objects.last()
        self.assertEqual(task.title, 'new')