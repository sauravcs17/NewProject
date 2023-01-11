from django.contrib.auth.models import User
from django import forms
from .models import Students
#from .models import UserProfile
from django.forms.widgets import DateInput
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control','id':'search-bar','required':''}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control','id':'search-bar','required':''}))
    email = forms.EmailField(label='email',widget=forms.TextInput(attrs={'type':'email','placeholder':'Email','class':'form-control','id':'search-bar','required':''}))
    first_name = forms.CharField(label='first_name',widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control','id':'search-bar','required':''}))
    last_name = forms.CharField(label='last_name',widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'search-bar','required':''}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['Registration_Number']
    '''
class LoginForm(forms.Form):
    name = forms.CharField(max_length=20)
    registration_number = forms.CharField(max_length=20)
    #password = forms.CharField(widget=forms.PasswordInput())


class StudentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'User Name','class':'form-control','id':'search-bar','required':''}))
    name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Student Name','class':'form-control','id':'search-bar','required':''}))
    Phone = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Contact Number','class':'form-control','id':'search-bar','required':''}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'autocomplete':'off','type':'email','placeholder':'Email','class':'form-control','id':'search-bar','required':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'off','placeholder':'Password','class':'form-control','id':'search-bar','required':''}))
    #stream = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'search-bar','required':''}))
    address = forms.CharField(widget=forms.Textarea(attrs={'autocomplete':'off','placeholder':'Permenant Address','class':'form-control','id':'search-bar','required':''}))
    registration_number = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Registration Number','class':'form-control','id':'search-bar','required':''}))
    #scheme=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Scheme','class':'form-control','id':'search-bar','required':''}))
    #semester=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Semester','class':'form-control','id':'search-bar','required':''}))
    
    class Meta:
        model = Students
        fields = '__all__'
        exclude=['slug',]

