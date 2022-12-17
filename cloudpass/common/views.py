from datetime import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from common.forms import MainForm
from yandex.yandex_downloader import get_file


def index(request):
    template = 'index.html'
    form = MainForm(request.POST or None)
    if form.is_valid():
        link = form.cleaned_data.get('search_field')
        file_content, ext = get_file(link)
        filename = dt.now().strftime('%H-%M-%S-%d-%m-%Y')
        response = HttpResponse(file_content, headers={
            'Content-Disposition': f'attachment; filename="{filename}.{ext}"'
        }
        )
        return response
    context = {'form': form}
    return render(request, template, context)
