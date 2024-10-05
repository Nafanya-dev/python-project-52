from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label=_("First name"),
                                 max_length=150,
                                 required=True,),

    last_name = forms.CharField(label=_("Last name"),
                                max_length=150,
                                required=True,),

    username = forms.CharField(label=_("Username"),
                               max_length=150,
                               required=True,
                               help_text=_("""Required field. No more than
                                           150 characters. Only letters,
                                           numbers and symbols @/./+/-/_."""))

    password1 = forms.CharField(label=_("Password"),
                                required=True,
                                widget=forms.PasswordInput(
                                attrs={'autocomplete': 'new-password'}),
                                help_text=_("""Your password must contain
                                            at least 3 characters."""))

    password2 = forms.CharField(label=_("Password confirmation"),
                                required=True,
                                widget=forms.PasswordInput(
                                attrs={'autocomplete': 'new-password'}),
                                help_text=_("""To confirm, please enter your
                                            password again."""))

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance and self.instance.username == username:
            return username

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError(
                  _("A user with that username already exists."))

        return username
