from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

from task_manager.users.forms import RegisterUserForm


class UserListView(ListView):
    """
    Handles requests to ('/users/')
    Method GET Returns the HTML code of the users list page.
    """
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class RegisterUserView(CreateView):
    """
    Handles requests to ('/users/create/')

    Method GET Returns the HTML code of the registration page.

    Method POST Creates a new user and redirects to the login page ('/login/')
    """
    form_class = RegisterUserForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('login-page')


class UpdateUserView(UpdateView):
    form_class = RegisterUserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users-list-page')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk)


class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users-list-page')
    login_url = reverse_lazy('login-page')

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(self.get_login_url())
        else:
            messages.error(self.request, _("You do not have permission to change another user."))
            return redirect('users-list-page')
