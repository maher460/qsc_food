from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from qsc_food.models import Profile

class SignUpForm(UserCreationForm):
    sex = forms.ChoiceField(choices=Profile.GENDER_TYPE_OPTIONS, help_text='Required. Please choose your gender')
    age = forms.IntegerField(help_text='Required')
    weight = forms.IntegerField(help_text='Required.')
    height = forms.IntegerField(help_text='Required.')


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'sex', 'age', 'weight', 'height')