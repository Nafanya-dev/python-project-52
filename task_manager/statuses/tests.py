from task_manager.fixtures.status_test_case import StatusTestCase

from task_manager.statuses.models import Status


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
        self.assertEqual(Status.objects.count(), 1)

        response = self.client.post(self.create_url, self.create_data)
        self.assertRedirects(response, self.status_list_url)
        self.assertEqual(Status.objects.count(), 2)

        status = Status.objects.last()
        self.assertEqual(status.name, 'new')


class UpdateStatusViewTest(StatusTestCase):
    def test_update_status_view_without_authentication(self):
        response = self.client.get(self.update_url)
        self.assertRedirects(response, self.login_url)

    def test_update_status_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.update_create_template)

    def test_status_update(self):
        self.client.force_login(self.user)

        self.assertEqual(self.status.name, 'at work')
        response = self.client.post(self.update_url, self.update_data)
        self.assertRedirects(response, self.status_list_url)

        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'completed')


class DeleteStatusViewTest(StatusTestCase):
    def test_delete_status_view_without_authentication(self):
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.login_url)

    def test_delete_status_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.delete_template)

    def test_delete_status(self):
        self.client.force_login(self.user)

        response = self.client.post(self.delete_url)

        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
        self.assertRedirects(response, self.status_list_url)
