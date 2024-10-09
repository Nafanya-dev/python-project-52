from task_manager.fixtures.user_test_case import (UserRegisterTestCase,
                                                  UserUpdateDeleteTestCase)
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


User = get_user_model()


class RegisterUserViewTest(UserRegisterTestCase):
    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post(self.url, self.valid_data)
        self.assertRedirects(response, reverse_lazy('login-page'))

        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.username, "Mr_Blonde+1-@_.")

    def test_user_creation_invalid_data(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(User.objects.count(), 0)


class UpdateUserViewTest(UserUpdateDeleteTestCase):
    def test_update_user_view_without_authentication(self):
        response = self.client.get(self.update_url)
        self.assertRedirects(response,
                             reverse_lazy('login-page'))

    def test_update_user_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'users/update_register_user_form.html')

    def test_update_user_data(self):
        self.client.force_login(self.user)

        response = self.client.post(self.update_url, self.updated_data)
        self.assertRedirects(response, reverse_lazy('users-list-page'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "Mr_Pink")


class DeleteUserViewTest(UserUpdateDeleteTestCase):
    def test_delete_user_view_without_authentication(self):
        response = self.client.get(self.delete_url)
        self.assertRedirects(response,
                             reverse_lazy('login-page'))

    def test_delete_user_view_with_authentication(self):
        self.client.force_login(self.user)

        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'users/delete_user.html')

    def test_delete_user(self):
        self.client.force_login(self.user)

        response = self.client.post(self.delete_url)

        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
        self.assertRedirects(response, reverse_lazy('users-list-page'))
