from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Use the custom User model
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'phone_number']

    # Adding custom validation for the phone number
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be 10 digits long.")
        return phone_number
