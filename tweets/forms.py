from django import forms
from django.contrib.auth.models import User
from .models import Tweet
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"]) 
        if commit:
            user.save()
        return user


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

class CustomRegistrationForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=150)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user
