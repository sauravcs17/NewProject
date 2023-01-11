from django.db import models
from Accounts.models import Stream,Semester,Students

# Create your models here.
class Exams(models.Model):
    exam_name = models.CharField(max_length=50)
    stream=models.ForeignKey('Accounts.Stream',on_delete=models.SET_NULL,null=True)
    semester=models.ForeignKey('Accounts.Semester',on_delete=models.SET_NULL,null=True)
    scheme = models.CharField(max_length=20,null=True)
    no_of_ques = models.CharField(max_length=20)
    total_marks = models.CharField(max_length=20)
    time_duration = models.DurationField(default='00:00:00')

    def __str__(self):
        return str(self.exam_name)


class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE,default=1)
    question_number = models.PositiveIntegerField(default=1,null=True)
    marks = models.PositiveIntegerField(default=0,null=True)
    question = models.TextField(max_length=500,null=True)
    answer = models.TextField(null=True)

    def __str__(self):
        return str(self.question)


class Answers(models.Model):
    user=models.ForeignKey('Accounts.Students',on_delete=models.SET_NULL,null=True)
    registration_number=models.CharField(max_length=20,null=True)
    quest=models.ForeignKey('Question',on_delete=models.SET_NULL,null=True)
    que=models.CharField(max_length=650,null=True)
    content= models.TextField()


class Result(models.Model):
    name=models.CharField(max_length=20,null=True)
    registration_number=models.CharField(max_length=20,null=True)
    que=models.CharField(max_length=650,null=True)
    marks=models.FloatField(null=True)
    totalmarks=models.FloatField(null=True)


class FinalScore(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True,unique=True)
    registration_number=models.CharField(max_length=20,null=True,unique=True)
    totalmarks=models.FloatField(null=True)
