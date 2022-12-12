from django.shortcuts import render
from forms import MainForm


def index(request):
    form = MainForm()
    template = ...
