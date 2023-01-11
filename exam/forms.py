from django.contrib.auth.models import User
from django import forms
from .models import Exams,Question,Answers,Result,FinalScore
#from .models import UserProfile
from django.forms.widgets import DateInput



class ExamForm(forms.ModelForm):
    exam_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Exam Name','class':'form-control','id':'search-bar','required':''}))
    #stream = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Stream','class':'form-control','id':'search-bar','required':''}))
    scheme = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Scheme','class':'form-control','id':'search-bar','required':''}))
    no_of_ques = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number of Questions','class':'form-control','id':'search-bar','required':''}))
    #stream = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'search-bar','required':''}))
    total_marks = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Total Marks','class':'form-control','id':'search-bar','required':''}))
   
    class Meta:
        model = Exams
        fields = '__all__'


class QuestionForm(forms.ModelForm):
   # exam_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Exam Name','class':'form-control','id':'search-bar','required':''}))
    #stream = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Stream','class':'form-control','id':'search-bar','required':''}))
    #marks = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Marks','class':'form-control','id':'search-bar','required':''}))
    question = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Question','class':'form-control','id':'search-bar','required':''}))
    #stream = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','id':'search-bar','required':''}))
    #answer = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Answer','class':'form-control','id':'search-bar','required':''}))
    

    class Meta:
        model = Question
        fields = '__all__'
        exclude=['marks','answer']


class AnswerForm(forms.ModelForm):
   
    
    #user= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'user'}))
    content = forms.CharField(label='',widget=forms.Textarea(attrs={ 'rows': 8,'cols':2,'placeholder':'Answer','name':'n2','id':'n2','required':''}))
   
    class Meta:
        model = Answers
        fields = '__all__'
        exclude=['user','registration_number','que','quest',]

class ResultForm(forms.ModelForm):
    marks = forms.IntegerField(label='',widget=forms.TextInput(attrs={'autocomplete':'off','maxlength':"4" ,'placeholder':'Enter Mark..','required':''}))

   
    class Meta:
        model = Result
        fields = '__all__'
        exclude=['name','registration_number','que','totalmarks']


'''
class FinalForm(forms.ModelForm):
     #marks = forms.IntegerField(label='',widget=forms.TextInput(attrs={'autocomplete':'off','maxlength':"4" ,'placeholder':'Enter Mark','required':''}))
    registration_number = forms.CharField(widget=forms.TextInput(attrs={'name':'q'}))
 
   
    class Meta:
        model = FinalScore
        fields = '__all__'
        exclude=['totalmarks']
'''