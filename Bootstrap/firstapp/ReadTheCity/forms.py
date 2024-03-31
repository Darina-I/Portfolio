from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeForm
import re

from django.core.exceptions import ValidationError

from .models import Profile, Book
from .validators import clean_password, clean_email, clean_year, clean_isbn


class AddBookForm(forms.ModelForm):
    name = forms.CharField(label='Название',widget=forms.TextInput(attrs={'class':'form-control'}))
    year = forms.CharField(label='Год выпуска',widget=forms.TextInput(attrs={'class':'form-control'}),validators=[clean_year])
    isbn = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),validators=[clean_isbn])
    content = forms.CharField(label='Краткое описание',widget=forms.Textarea(attrs={'cols': 30, 'rows': 2, 'class':'form-control'}))

    class Meta:
        model = Book
        fields = ['name','authors','photo','content','print','year','genre','lang','isbn']
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
        }
class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин',
               widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:#явная связка с моделью
        model = get_user_model()
        fields= ['username', 'password']

class RegisterUserForm(forms.ModelForm):#будет работать с моделью, поэтому ModelForm
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='E-mail',validators=[clean_email])
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(),validators=[clean_password])
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields= ['username', 'email', 'password', 'password2']
        label = {
            'email': 'E-mail',
        }

    #проверяется равенство паролей
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError("Пароли не совпадают")
        else:
            return password

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField( required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    birth = forms.DateField( required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата рождения')
    city = forms.CharField( required=False, max_length=20,label='Город', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField( required=False, max_length=20,label='О себе', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['birth', 'photo', 'city', 'content']

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}),validators=[clean_password])
    new_password2 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        password = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password != password2:
            raise ValidationError("Пароли не совпадают")
        else:
            return password