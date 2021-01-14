from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput,required=False)
        
    def clean(self):
 
        # data from the form is fetched using super function
        super(CreateUserForm, self).clean()
         
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
 
        # conditions to be met for the password1
        if len(password1) < 8:
            self._errors['password1'] = self.error_class([
                'password:Minimum 8 characters required'])

        if len(re.sub('[\w\d]+' ,'', password1)) < 2:
            self._errors['password1'] = self.error_class([
                'password:Minimum 2 special characters required'])

        if not re.findall('.*\\d{2,}', password1):
            self._errors['password1'] = self.error_class([
                'password:Minimum 2 digits required'])

        # return any errors if found
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class QueryForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    query = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your query!'
    )

    def clean(self):
        cleaned_data = super(QueryForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        query = cleaned_data.get('query')
        if not name and not email and not query:
            raise forms.ValidationError('You have to write something!')