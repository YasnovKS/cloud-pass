from datetime import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from common.exceptions import ResponseException, WrongLinkException
from common.forms import MainForm
from common.messages import MANUAL, ATTENTION
from common. links_handler import Link


def index(request):
    template = 'index.html'
    form = MainForm(request.POST or None)
    context = {'form': form,
               'message': MANUAL,
               'attention': ATTENTION,
               }
    if form.is_valid():
        form_data = form.cleaned_data.get('search_field')
        link = Link(form_data)
        try:
            downloader = link.get_downloader()
            get_file = getattr(downloader, 'get_file')
            file_content, ext = get_file(form_data)
        except (ResponseException, WrongLinkException) as e:
            context['link_error'] = e
            return render(request, template, context)
        filename = dt.now().strftime('%H-%M-%S-%d-%m-%Y')
        response = HttpResponse(file_content, headers={
            'Content-Disposition': f'attachment; filename="{filename}.{ext}"'
        }
        )
        return response
    return render(request, template, context)
