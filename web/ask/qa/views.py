from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from .models import Answer, Question


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, query_set, default_page=1, default_limit=10, max_limit=20):
    try:
        limit = int(request.GET.get('limit', default_limit))
    except ValueError:
        limit = default_limit
    limit = min(limit, max_limit)

    try:
        page_number = int(request.GET.get('page', default_page))
    except ValueError:
        page_number = 1
    paginator = Paginator(query_set, limit)

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page, paginator


@require_GET
def list_recent_questions(request):
    questions = Question.objects.recent()
    page, paginator = paginate(request, questions, default_page=1, default_limit=10)
    return render(request, 'qa/recent_questions.html', context={
        'questions': questions,
        'paginator': paginator,
        'page': page
    })


@require_GET
def list_popular_questions(request):
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions, default_page=1, default_limit=10)
    return render(request, 'qa/popular_questions.html', context={
        'questions': questions,
        'paginator': paginator,
        'page': page
    })


@require_GET
def show_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)

    return render(request, 'qa/question.html', context={
        'question': question,
        'answers': answers
    })
