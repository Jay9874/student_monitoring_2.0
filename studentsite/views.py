from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student, Score, Cocurriculum, Achievement, Remark
import sys; sys.stdout.flush()




def student_home(request):
    student = Student.objects.filter(student=request.user.id)
    # student_obj = Student.objects.get(admin=request.user.id)
    # total_subjects = Subjects.objects.filter(student_id=student.id)

    # subject_name = []
    context = {
        "student_list": student
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/home.html", context)


def scores(request):
    student = Student.objects.get(student=request.user.id)
    scores = Score.objects.filter(student=student).values()
    for value in scores:
        print(value)
    # for score in scores:
    #     print(score.values())
    # semester = Semester.objects.filter(score=score, student=student)

    context = {
        "student_list": student,
        "scores": scores,
        # "semesters": semester 
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/scores.html", context)



def analytics(request):
    student = Student.objects.filter(student=request.user.id)
    # # student_result = Score.objects.filter(student_id=student.id)

    context = {
        "student_list": student
    }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/analytics.html", context)


def cocurriculum(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/cocurriculum.html", context)


def achievement(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "achievements/academics.html", context)

def remark(request):
    student = Student.objects.filter(student=request.user.id)

    context = {
        "student_list": student
    
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/remark.html", context)