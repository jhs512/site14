from django.http import HttpResponse
from django.shortcuts import render

from pybo.models import Question


def index(request):
    question_list = Question.objects.order_by('-id')

    context = {'question_list' : question_list}

    return render(request, 'pybo/question_list.html', context)