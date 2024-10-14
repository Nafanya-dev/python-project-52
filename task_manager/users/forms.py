from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# module with texts for buttons, flash messages, titles
from task_manager import texts


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label=texts.FIRST_NAME_LABEL_USER_FORM,
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': texts.FIRST_NAME_LABEL_USER_FORM}))

    last_name = forms.CharField(
        label=texts.LAST_NAME_LABEL_USER_FORM,
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2',
                   'placeholder': texts.LAST_NAME_LABEL_USER_FORM}))

    username = forms.CharField(
        label=texts.USERNAME_LABEL_USER_FORM,
        max_length=150,
        required=True,
        help_text=texts.USERNAME_HELP_TEXT_USER_FORM,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2',
                   'placeholder': texts.USERNAME_LABEL_USER_FORM}))

    password1 = forms.CharField(
        label=texts.PASSWORD1_LABEL_USER_FORM,
        required=True,
        help_text=texts.PASSWORD1_HELP_TEXT_USER_FORM,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control mt-2',
                   'placeholder': texts.PASSWORD1_LABEL_USER_FORM}))

    password2 = forms.CharField(
        label=texts.PASSWORD2_LABEL_USER_FORM,
        required=True,
        help_text=texts.PASSWORD2_HELP_TEXT_USER_FORM,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'form-control mt-2',
                   'placeholder': texts.PASSWORD2_LABEL_USER_FORM}))

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
                  texts.USERNAME_VALIDATION_ERROR_MESSAGE_USER_FORM)

        return username
