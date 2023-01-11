from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
import os
from .models import Exams,Question,Answers,Result,FinalScore
from Accounts.models import Students
from .forms import ExamForm,QuestionForm,AnswerForm
from django.core.paginator import Paginator
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Q
from django.db import IntegrityError
from django.shortcuts import render_to_response

# Create your views here.



#def startexam(request):
  #  return render(request,"exam1.html")

def exam(request):
    if request.session.has_key('z'):
        #us = request.session['z']
        a = request.session['z']
        std = Students.objects.filter(name=a)
        question=Question.objects.all()
        paginator = Paginator(question, 1)  # Show 25 contacts per page
        page = request.GET.get('page')
        #reg=request.POST.get['registration_number']
        #exam_name = request.GET.get('exam_name')
        question = paginator.get_page(page)
        #quest=Question.objects.filter(id=2)
        if request.method == 'POST':
             answer =AnswerForm(data=request.POST)
             if answer.is_valid():
                  instance=answer.save(commit=False)
                  instance.user=std.first()
                  for k in question:
                      v=k.question
                      instance.que=v
                  for i in std:
                      s= i.registration_number
                      instance.registration_number=s

                  instance.save()
        else:
            answer = AnswerForm()
        answ=Answers.objects.all()
        #instance = get_object_or_404(Students, name=a)
    #question=Question.objects.all()
    #paginator = Paginator(question, 1)  # Show 25 contacts per page
    #page = request.GET.get('page')
    #question = paginator.get_page(page)
   
    for i in std:
        print("students",i.registration_number)
  
    context = {
            'question': question,
            'student':std,
            'exam':exam,
            'answers': answer,
            'answ':answ
            #'instance':instance
        }
    return render(request,"onlinetest.html",context)
     
'''
            if request.POST.get('n2'):
                post=Answers()
               # post.user_id=request.user.get.GET('name')
                post.content= request.POST.get('n2')
                post.save()
                
                #return redirect('/exams/start/') 
'''
 
'''
def exam(request):
    if request.session.has_key('z'):
       # name = request.GET.get('name')
       # request.session['name'] = name
        a = request.session['z']
        user = Students.objects.filter(name=a)
        question = Question.objects.get_queryset().order_by('id')
       # student=Students.objects.all()
        
        paginator = Paginator(question, 1)  # Show 25 contacts per page

        page = request.GET.get('page')
        question = paginator.get_page(page)
        exam=Exams.objects.all()
        instance = get_object_or_404(Students, user=a)
        if request.method == 'POST':
            if request.POST.get('output'):
                post=Post()
                #post.title= request.POST.get('title')
                post.content= request.POST.get('output')
                post.save()
                
                return redirect('/')  

    
        
        context = {
            'question': question,
            'student':user,
            'exam':exam,
            'ur': a,
            'instance': instance,
            #'exam_name': name,
        }
     
    return render(request, 'rough.html', context)

'''



def createquestion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question_form = QuestionForm(data=request.POST, files=request.FILES)
            if question_form.is_valid():
                instance = question_form.save(commit=False)
                if instance.question_number is not None:
                    instance.question_number = instance.question_number + 1
                instance.save()

                messages.info(request, "Successfully Added Question")
                return redirect('/exams/addquestion')
        else:
            question_form = QuestionForm()

    return render(request, 'addquestion.html', {'question': question_form})

def questionlist(request):
    question=Question.objects.all()
    context={
        "questionlist":question
    }
    return render(request,"questionslist.html",context)

def about(request):
    
    return render(request,"about.html")
def thankyou(request):
    return render(request,"thankyou.html")




def result(request):
    final=FinalScore.objects.all()
    try:
        if request.method == 'POST':
            if request.POST.get('q'):
                post=FinalScore()
                abc=request.POST.get('q')
                post.name= request.POST.get('n1')
                post.registration_number= abc
                post.totalmarks=Result.objects.filter(registration_number=abc).aggregate(Sum('marks'))['marks__sum'] or 0
                post.save()
    except IntegrityError as e:
        e="Result already Added"
        return render(request,"resulttable.html", {"message": e})

    context={
        "finalscore":final
    }
                
    return render(request,"resulttable.html",context)


def finaloutput(request):

    score=FinalScore.objects.all()
    search_query=request.GET.get('q')
    if search_query:
        score=FinalScore.objects.filter(registration_number=search_query)
    context={
        "score":score
    }
    return render(request,"finalscore.html",context)



