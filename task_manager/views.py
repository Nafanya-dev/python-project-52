from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth.forms import AuthenticationForm


class HomeView(View):
    """
    Handles requests to ('/').

    Method GET Returns the HTML code of the main page.
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginUserView(LoginView):
    """
    Handles requests to ('/login/').

    Method GET Returns the HTML code of the login page.
    Method POST authenticates the user
    Upon successful authentication, redirects to the main page ('/')
    """
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy("home-page")
