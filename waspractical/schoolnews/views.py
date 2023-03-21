from django.shortcuts import render
from django.http import HttpResponse
from schoolnews.models import Page

def index(request):
    pages_list = Page.objects.order_by('-date')[:5]

    context_dict = {}
    context_dict['pages'] = pages_list

    return render(request, 'schoolnews/index.html', context=context_dict)
