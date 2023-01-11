"""Drishti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name='exam'

urlpatterns = [
   
    path('start/',views.exam,name='startexam'),
    path('finalresult/',views.finaloutput,name="finalresult"),
    path('addquestion/',views.createquestion,name='addquestion'),
    path('questionlist/',views.questionlist,name='questionlist'),  
    path('result/',views.result,name="result"),
  
    #path('final/',views.finalscore,name='finalscore'),
    path('about/',views.about,name='about'),
    path('completed/',views.thankyou,name='completed')
   # path('addquestion/',views.createquestion,name='addquestion')
   # path('speech/', views.hai, name='speech'),
    
    

]
