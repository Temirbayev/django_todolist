from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Импортируйте модель User


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # Поля, которые вы хотите отображать в форме

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Настройка полей формы, если необходимо
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
