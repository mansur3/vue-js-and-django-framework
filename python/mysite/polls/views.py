from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import F


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {
        "latest_question_list": latest_question_list,
    }

    return HttpResponse(template.render(context, request))
  
def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    questionObject = {
        'questionTitle': question
    }
    print('questionObject', questionObject)
    return render(request, 'polls/detail.html', questionObject )
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # choice = question.choice_set.get(Choice, question)
    print('question', question)
    choice = Choice.objects.filter(question=question.id)
    print('choice', choice)


    responsed = "You're looking at the results of question ."

    return HttpResponse(responsed)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render( 
            request,
            "polls/form.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            }
        )
    else:
        print("question id", question.id)
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    # return HttpResponse("You're voting on question.")

