from django.shortcuts import render
from django.conf import settings


meta = {
    'title': '',
    'description': '',
    'image': ''
}


def home(request):
    data = {}
    data['META'] = settings.DEFAULT_META
    return render(request, 'base.html', data)
