from django import forms
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'yab/index.html')


def name(request):
    if request.POST:
        name_from_form = request.POST.get('your_name')
        # return HttpResponse(name_from_form)
        return render(request, 'yab/index.html', {'current_name': name_from_form})
    else:
        return render(request, 'yab/index.html')
