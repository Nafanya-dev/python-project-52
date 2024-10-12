from task_manager.fixtures.user_test_case import UserTestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterUserViewTest(UserTestCase):
    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

        response = self.client.post(self.urls.get('create_url'),
                                    self.data.get('Valid_data'))

        self.assertRedirects(response, self.urls.get('login_url'))
        self.assertEqual(User.objects.count(), 2)

        user = User.objects.last()
        self.assertEqual(user.username,
                         self.data.get('Valid_data')['username'])

    def test_user_creation_invalid_data(self):
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post(self.urls.get('create_url'),
                                    self.data.get('Invalid_data'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)


class UpdateUserViewTest(UserTestCase):
    def test_update_user_view_without_authentication(self):
        response = self.client.get(self.urls.get('update_url'))
        self.assertRedirects(response, self.urls.get('login_url'))

    def test_update_user_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('update_url'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_update_user_data(self):
        self.client.force_login(self.user)

        response = self.client.post(self.urls.get('update_url'),
                                    self.data.get('Updated_data'))

        self.assertRedirects(response, self.urls.get('user_list_url'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.username,
                         self.data.get('Updated_data')['username'])


class DeleteUserViewTest(UserTestCase):
    def test_delete_user_view_without_authentication(self):
        response = self.client.get(self.urls.get('delete_url'))
        self.assertRedirects(response, self.urls.get('login_url'))

    def test_delete_user_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.urls.get('delete_url'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, self.templates.get('delete'))

    def test_delete_user(self):
        self.client.force_login(self.user)

        response = self.client.post(self.urls.get('delete_url'))
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

        self.assertRedirects(response, self.urls.get('user_list_url'))
