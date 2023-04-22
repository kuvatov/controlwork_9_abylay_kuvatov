from django import forms
from django.contrib.auth import get_user_model


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }
