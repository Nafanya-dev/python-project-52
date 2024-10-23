from task_manager.statuses.tests.status_test_case import StatusTestCase

from task_manager.statuses.models import Status


class CreateStatusViewTest(StatusTestCase):
    def test_create_status_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('create_url'))
        self.assertRedirects(response,
                             self.get_urls().get('login_url'))

    def test_create_status_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('create_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_status_creation(self):
        self.client.force_login(self.user)

        self.assertEqual(Status.objects.count(), 1)
        response = self.client.post(self.get_urls().get('create_url'),
                                    self.get_data().get('Create_data'))

        self.assertRedirects(response, self.get_urls().get('status_list_url'))
        self.assertEqual(Status.objects.count(), 2)

        status = Status.objects.last()
        self.assertEqual(status.name,
                         self.get_data().get('Create_data')['name'])


class UpdateStatusViewTest(StatusTestCase):
    def test_update_status_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('update_url'))
        self.assertRedirects(response, self.get_urls().get('login_url'))

    def test_update_status_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('update_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_status_update(self):
        self.client.force_login(self.user)

        self.assertEqual(self.status.name, 'In Progress')
        response = self.client.post(self.get_urls().get('update_url'),
                                    self.get_data().get('Updated_data'))

        self.assertRedirects(response, self.get_urls().get('status_list_url'))

        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'completed')


class DeleteStatusViewTest(StatusTestCase):
    def test_delete_status_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('delete_url'))
        self.assertRedirects(response, self.get_urls().get('login_url'))

    def test_delete_status_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('delete_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('delete'))

    def test_delete_status(self):
        self.client.force_login(self.user)

        self.assertEqual(Status.objects.count(), 1)
        response = self.client.post(self.get_urls().get('delete_url'))

        self.assertEqual(Status.objects.count(), 0)
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
        self.assertRedirects(response, self.get_urls().get('status_list_url'))
