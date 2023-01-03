from datetime import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from common.exceptions import ResponseException
from common.forms import MainForm
import google.google_downloader as google
import yandex.yandex_downloader as yandex


def parse_link(link):
    if 'yandex' in link:
        return yandex
    return google


def index(request):
    template = 'index.html'
    form = MainForm(request.POST or None)
    if form.is_valid():
        link = form.cleaned_data.get('search_field')
        try:
            file_content, ext = parse_link(link).get_file(link)
        except ResponseException as e:
            return HttpResponse(e)
        filename = dt.now().strftime('%H-%M-%S-%d-%m-%Y')
        response = HttpResponse(file_content, headers={
            'Content-Disposition': f'attachment; filename="{filename}.{ext}"'
        }
        )
        return response
    context = {'form': form}
    return render(request, template, context)
