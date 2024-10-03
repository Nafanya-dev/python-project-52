from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 label=_("First name")),

    last_name = forms.CharField(max_length=30,
                                required=True,
                                label=_("Last name")),

    username = forms.CharField(max_length=150,
                               required=True,
                               label=_("Username"),
                               help_text=_("""Required field. No more than
                                           150 characters. Only letters,
                                           numbers and symbols @/./+/-/_."""))

    password2 = forms.CharField(label=_("Password confirmation"),
                                required=True,
                                widget=forms.PasswordInput(
                                attrs={'autocomplete': 'new-password'}),
                                help_text=_("""To confirm, please enter your
                                            password again."""))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

        labels = {
            'password1': _("Password"),
        }

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance and self.instance.username == username:
            return username

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                  _("A user with that username already exists."))

        return username
