from datetime import datetime as dt

from django.http import FileResponse
from django.shortcuts import render

from common.forms import MainForm
from yandex.yandex_downloader import DIRECTORY, get_file


def index(request):
    template = 'index.html'
    form = MainForm(request.POST or None)
    if form.is_valid():
        link = form.cleaned_data.get('search_field')
        file_content, ext = get_file(link)
        filename = dt.now().strftime('%H-%M-%S-%d-%m-%Y')
        file_path = DIRECTORY / f'{filename}.{ext}'
        with open(file_path, 'wb') as file:
            file.write(file_content)
        response = FileResponse(open(file_path, 'rb'),
                                as_attachment=True,
                                filename=f'{filename}.{ext}')
        return response
    context = {'form': form}
    return render(request, template, context)
