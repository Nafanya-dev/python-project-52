from task_manager.fixtures.label_test_case import LabelTestCase

from task_manager.labels.models import LabelModel


class CreateLabelViewTest(LabelTestCase):
    def test_create_label_view_without_authentication(self):
        response = self.client.get(self.urls.get('create_url'))
        self.assertRedirects(response,
                             self.urls.get('login_url'))

    def test_create_label_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('create_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_label_creation(self):
        self.client.force_login(self.user)

        self.assertEqual(LabelModel.objects.count(), 1)
        response = self.client.post(self.urls.get('create_url'), self.data.get('Create_data'))
        self.assertRedirects(response, self.urls.get('label_list_url'))
        self.assertEqual(LabelModel.objects.count(), 2)

        status = LabelModel.objects.last()
        self.assertEqual(status.name, self.data.get('Create_data')['name'])


class UpdateLabelViewTest(LabelTestCase):
    def test_update_label_view_without_authentication(self):
        response = self.client.get(self.urls.get('update_url'))
        self.assertRedirects(response, self.urls.get('login_url'))

    def test_update_label_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('update_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_label_update(self):
        self.client.force_login(self.user)

        self.assertEqual(self.label.name, 'at work')
        response = self.client.post(self.urls.get('update_url'),
                                    self.data.get('Updated_data'))

        self.assertRedirects(response, self.urls.get('label_list_url'))

        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'completed')


class DeleteLabelViewTest(LabelTestCase):
    def test_delete_label_view_without_authentication(self):
        response = self.client.get(self.urls.get('delete_url'))
        self.assertRedirects(response, self.urls.get('login_url'))

    def test_delete_label_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('delete_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                self.templates.get('delete'))

    def test_delete_label(self):
        self.client.force_login(self.user)

        response = self.client.post(self.urls.get('delete_url'))

        self.assertFalse(LabelModel.objects.filter(pk=self.label.pk).exists())
        self.assertRedirects(response, self.urls.get('label_list_url'))
