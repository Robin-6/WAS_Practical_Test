from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'message': 'Placeholder message'}
    return render(request, 'schoolnews/index.html', context=context_dict)
