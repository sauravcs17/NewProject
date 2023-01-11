from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Stream,Students
from .forms import LoginForm,StudentForm
from exam.forms import ResultForm
from exam.models import Exams,Answers,Result,Question
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Avg, Max, Min, Sum
# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'index2.html')


# Create your views here.

def login(request):
    if request.method == 'POST':
        exam = Exams.objects.all()
        username = request.POST['name1']
        registration_number = request.POST['reg1']

        user = Students.objects.filter(name=username,registration_number=registration_number)
        if not user:
            messages.info(request, "invalid credentials")
            
            return redirect('/accounts/login')

        else:
            #messages.info(request, "login successfull")
            request.session['z'] = username
            request.session.get_expiry_age()
            instance = get_object_or_404(Students, name=username)
            return render(request, 'exam1.html',{'exam': exam, 'ur': username, 'instance': instance})
    else:
        return render(request, 'login.html')


def instruction(request):
    return render(request,"exam1.html")



'''
def profile(request):
    user=Student.objects.all()
    return render(request,"profile.html",{'user':user})
'''


def profile(request):
    if request.session.has_key('z'):
        us = request.session['z']
       # name = request.session['name']
        user = Students.objects.filter(name=us)
        instance = get_object_or_404(Students, name=us)
        context = {
            'user': user,
            'ur': us,
            'instance': instance,
            #'exam_name': name,
        }
        return render(request, 'profile.html', context)

def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            # return render(request,'defaultlogin.html',{'username':username})
            return redirect('/accounts/adminduty')
            # return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/accounts/authlogin')
    else:
         return render(request,"loginauth.html")



def adminduty(request):
    '''
    search_query = request.GET.get('q')
    if search_query:
        std = Students.filter(
            Q(name__icontains=search_query) 
        )
    context={'student_list':std}
    '''
    return render(request,"staffhome.html")  

def addstudent(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            student_form =StudentForm(data=request.POST, files=request.FILES)
            if student_form.is_valid():
                student_form.save()
                messages.info(request, "Successfully Added Student")
                return redirect('/accounts/addstudent')
        else:
            student_form = StudentForm()

    return render(request, 'addstudent.html', {'student': student_form})

'''
def studentlist(request):
    #student=Students.objects.all()
    #lname=request.GET.get('user_id')
    question=Question.objects.all()
 
    answer=Answers.objects.all()
    details="NO DETAILS FOUND....."
    #for i in answ:
        #print(i)

    search_query = request.GET.get('q')
    if search_query:
        answer=Answers.objects.filter(registration_number=search_query)
    else:
        #s=messages.info(request, "No Details Found")
        details=details
    if request.method == 'POST':
        result =ResultForm(data=request.POST)
        if result.is_valid():
            instance=result.save(commit=False)
            for k in answer:
                v=k.que
                instance.que=v
            for i in answer:
                s= i.registration_number
                v=i.user
                instance.registration_number=s
                instance.name=v

            instance.save()
    else:
        result = ResultForm()
    context={
        "answer_list":answer,
        "details":details,
        "result":result
        
    }
    return render(request,"answerlist.html",context)
'''
def studentlist(request):
    #student=Students.objects.all()
    #lname=request.GET.get('user_id')
 
    answer=Answers.objects.all()
   
    details="NO DETAILS FOUND....."
    #for i in answ:
        #print(i)
    search_query = request.GET.get('q')
    if search_query:
        answer=Answers.objects.filter(registration_number=search_query)
       
    else:
        #s=messages.info(request, "No Details Found")
        details=details
    paginator = Paginator(answer, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    answer = paginator.get_page(page)
    if request.method == 'POST':
        result =ResultForm(data=request.POST)
        if result.is_valid():
            instance=result.save(commit=False)
    
            for k in answer:
                v=k.que
                instance.que=v
            for i in answer:
                s= i.registration_number
                v=i.user
                instance.registration_number=s
                instance.name=v

            instance.save()
            messages.info(request,"Mark Added Successfully")
    else:
        result = ResultForm()
    context={
        "answer_list":answer,
        "details":details,
        "result":result
        
    }
    return render(request,"answerlist.html",context)


def liststudents(request):
    student=Students.objects.all()
    context={
        "students":student
    }
    return render(request,"stdlist.html",context)

'''
    if search_query:
        student = student.filter(
            Q(name__icontains=search_query) |
            Q(registration_number__icontains=search_query)

        )

    context={
        "student_list":student,
        "answ":answ
    }

    return render(request,"studentlist.html",context)
'''
