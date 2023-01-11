from django.contrib import admin
from . models import Exams,Question,Answers,Result,FinalScore
# Register your models here.
admin.site.register(Exams)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Result)
admin.site.register(FinalScore)