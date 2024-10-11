from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy

# module with texts for buttons, flash messages, titles
from task_manager import texts


class AuthorizationRequiredMixin(LoginRequiredMixin):
    """
    inherits from LoginRequiredMixin and checks
    whether the user is authenticated.
    If not, it displays an error message and redirects to the login page
    """
    authorization_message = texts.AUTHORIZATION_MESSAGE

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.authorization_message)
            return redirect(reverse_lazy('login-page'))

        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(UserPassesTestMixin):
    """
    inherits from UserPassesTestMixin and checks whether
    the current user has access to the object. If not,
    then displays an error message and redirects to
    user list page
    """
    permission_message = None

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(reverse_lazy('users-list-page'))


class AuthorDeletionMixin(UserPassesTestMixin):
    author_message = None
    author_url = None

    def test_func(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        messages.error(self.request, self.author_message)
        return redirect(self.author_url)


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
