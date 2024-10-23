from task_manager.users.tests.user_test_case import UserTestCase
from django.contrib.auth import get_user_model


USER = get_user_model()


class RegisterUserViewTest(UserTestCase):
    def test_user_creation(self):
        self.assertEqual(USER.objects.count(), 2)

        response = self.client.post(self.get_urls().get('create_url'),
                                    self.get_data().get('Valid_data'))

        self.assertRedirects(response, self.get_urls().get('login_url'))
        self.assertEqual(USER.objects.count(), 3)

        user = USER.objects.last()
        self.assertEqual(user.username,
                         self.get_data().get('Valid_data')['username'])

    def test_user_creation_invalid_data(self):
        self.assertEqual(USER.objects.count(), 2)
        response = self.client.post(self.get_urls().get('create_url'),
                                    self.get_data().get('Invalid_data'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(USER.objects.count(), 2)


class UpdateUserViewTest(UserTestCase):
    def test_update_user_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('update_url'))
        self.assertRedirects(response, self.get_urls().get('login_url'))

    def test_update_user_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('update_url'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response,
                                self.templates.get('update_create_form'))

    def test_update_user_data(self):
        self.client.force_login(self.user)

        response = self.client.post(self.get_urls().get('update_url'),
                                    self.get_data().get('Updated_data'))

        self.assertRedirects(response, self.get_urls().get('user_list_url'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.username,
                         self.get_data().get('Updated_data')['username'])


class DeleteUserViewTest(UserTestCase):
    def test_delete_user_view_without_authentication(self):
        response = self.client.get(self.get_urls().get('delete_url'))
        self.assertRedirects(response, self.get_urls().get('login_url'))

    def test_delete_user_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.get_urls().get('delete_url'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, self.templates.get('delete'))

    def test_delete_user(self):
        self.client.force_login(self.user)

        self.assertEqual(USER.objects.count(), 2)
        response = self.client.post(self.get_urls().get('delete_url'))

        self.assertEqual(USER.objects.count(), 1)
        self.assertFalse(USER.objects.filter(pk=self.user.pk).exists())

        self.assertRedirects(response, self.get_urls().get('user_list_url'))
