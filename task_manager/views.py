from django.shortcuts import render
from django.views import View


class HomeView(View):
    """
    Handles requests to ('/')
    Method GET Returns the HTML code of the main page.
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
