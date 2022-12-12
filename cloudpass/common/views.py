from django.shortcuts import render
from forms import MainForm


def index(request):
    template = 'index.html'
    form = MainForm(request.POST or None)
    if form.is_valid():
        link = form.cleaned_data.get('search_field')
