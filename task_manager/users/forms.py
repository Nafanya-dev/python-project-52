from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


FIRST_NAME_LABEL_USER_FORM = _("First name")
LAST_NAME_LABEL_USER_FORM = _("Last name")
USERNAME_LABEL_USER_FORM = _("Username")
PASSWORD1_LABEL_USER_FORM = _("Password")
PASSWORD2_LABEL_USER_FORM = _("Password confirmation")

USERNAME_HELP_TEXT_USER_FORM = _("""Required field. No more than 150 characters. Only letters,
                                    numbers and symbols @/./+/-/_.""")

PASSWORD1_HELP_TEXT_USER_FORM = _("Your password must contain at least 3 characters.")
PASSWORD2_HELP_TEXT_USER_FORM = _("To confirm, please enter your password again.")
USERNAME_VALIDATION_ERROR_MESSAGE_USER_FORM = _("A user with that username already exists.")


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label=FIRST_NAME_LABEL_USER_FORM,
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': FIRST_NAME_LABEL_USER_FORM}))

    last_name = forms.CharField(
        label=LAST_NAME_LABEL_USER_FORM,
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2',
                   'placeholder': LAST_NAME_LABEL_USER_FORM}))

    username = forms.CharField(
        label=USERNAME_LABEL_USER_FORM,
        max_length=150,
        required=True,
        help_text=USERNAME_HELP_TEXT_USER_FORM,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2',
                   'placeholder': USERNAME_LABEL_USER_FORM}))

    password1 = forms.CharField(
        label=PASSWORD1_LABEL_USER_FORM,
        required=True,
        help_text=PASSWORD1_HELP_TEXT_USER_FORM,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control mt-2',
                   'placeholder': PASSWORD1_LABEL_USER_FORM}))

    password2 = forms.CharField(
        label=PASSWORD2_LABEL_USER_FORM,
        required=True,
        help_text=PASSWORD2_HELP_TEXT_USER_FORM,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control mt-2',
                   'placeholder': PASSWORD2_LABEL_USER_FORM}))

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
                  USERNAME_VALIDATION_ERROR_MESSAGE_USER_FORM)

        return username
