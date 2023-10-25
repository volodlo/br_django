from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        help_text=' Формат +7...', label='Номер телефона'
    )
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', )