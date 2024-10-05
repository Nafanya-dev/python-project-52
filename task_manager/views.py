from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import AuthenticationForm


LOGIN_SUCCESS_MESSAGE = _("You are logged in")


class HomeView(View):
    """
    URL ('/')
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginUserView(SuccessMessageMixin, LoginView):
    """
    URL ('login/')

    Method GET Returns the HTML code of the login page
    Method POST authenticates the user and redirects to the main page ('/')
    """
    form_class = AuthenticationForm
    template_name = 'login.html'
    next_page = "home-page"

    success_message = LOGIN_SUCCESS_MESSAGE


class LogoutUserView(LogoutView):
    """
    URL ('logout/')

    Method POST logs the user out and redirects to main page ('/')
    """
    next_page = 'home-page'

    def post(self, request, *args, **kwargs):
        messages.info(request, "You have been successfully logged out.")
        return super().post(request, *args, **kwargs)
