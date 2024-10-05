from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class AuthorizationRequiredMixin(LoginRequiredMixin):
    """
    inherits from LoginRequiredMixin and checks
    whether the user is authenticated.
    If not, it displays an error message and redirects to the login page
    """
    authorization_message = None

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
