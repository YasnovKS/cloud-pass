from common.forms import MainForm
from django.http import HttpResponse, FileResponse, StreamingHttpResponse

from django.shortcuts import render
from yandex.yandex_downloader import get_file, DIRECTORY
from datetime import datetime as dt


def index(request):
    template = 'index.html'
    form = MainForm(request.POST or None)
    if form.is_valid():
        link = form.cleaned_data.get('search_field')
        file_content, ext, content_type = get_file(link)
        filename = dt.now().strftime('%H-%M-%S-%d-%m-%Y')
        file_path = DIRECTORY / f'{filename}.{ext}'
        with open(file_path, 'wb') as file:
            file.write(file_content)
        response = FileResponse(open(file_path))
        response['Content-Disposition'] = ('attachment; '
                                           f'filename={filename}.{ext}')
        return response
    context = {
        'form': form,
    }
    return render(request, template, context)
