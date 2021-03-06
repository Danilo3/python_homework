from django import forms
from django.contrib.auth.models import User

from .models import Profile, Booking


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    # username = forms.CharField(label='Username', min_length=5)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class BookingRoomForm(forms.ModelForm):
    from_date = forms.DateField(label="Arrival Date")
    to_date = forms.DateField(label="Departure Date")
    class Meta:
        model = Booking
        fields = ( 'adults_count', 'children_count')