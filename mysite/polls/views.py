from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question,Choice
from django.template import loader


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {
            "latest_question_list": latest_questions,
    }
    return render(request,"polls/index.html",context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question.question_text})
def results(request,question_id):
    return HttpResponse("You are looking at the results of question %s."% question_id)

def vote(request,question_id):
    return HttpResponse("You are voting for the question %s."% question_id)



