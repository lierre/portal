from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username or Email", max_lenght=30,
                               widget=forms.TextInput(attrs={'class': 'form-input'}),
                               error_messages={'required': 'Please enter a username'})
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}),
                               required=False)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data('username', '').lower()
        password = self.cleaned_data('password', '').lower()

        if '@' in username:
            user = User.objects.filter(email=username)
            if not user:
                user = User.objects.filter(email__iexact=username)
        else:
            user = User.objects.filter(username=username)
            if not user:
                user = User.objects.filter(username__iexact=username)
        if user:
            user = user[0]
        if username and password

