from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')
