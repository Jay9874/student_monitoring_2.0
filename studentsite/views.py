from django.shortcuts import render
from collections import defaultdict
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
    total = 0
    percent = 0
    filteredScore = defaultdict(int)
    for key, value in scores[0].items():
        if key not in('id', 'student_id'):
            total += value
            subject_name = list(key.split("_"))
            filteredScore[subject_name[0].capitalize()] += value
                
    percent = round((total/700) * 100, 2)
    context = {
        "student_list": student,
        "scores": filteredScore.items(),
        "total": total,
        "percent": percent
        # "semesters": semester 
    }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite/scores.html", context)



def analytics(request):
    student = Student.objects.get(student=request.user.id)
    scores = Score.objects.filter(student=student).values()
    filteredScore = {}
    for key, value in scores[0].items():
        if key not in('id', 'student_id'):
            subject_name = list(key.split("_"))[0].capitalize()
            if subject_name in filteredScore:
                filteredScore[subject_name] += value
            else:
                filteredScore[subject_name] = value
    print(filteredScore)
    context = {
        "student_list": student,
         "scores": filteredScore,
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