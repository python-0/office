from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Files

from django.views.generic import View


class IndexView(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        files = search(page)
        return render(request, 'index.html', {'files': files})

    def post(self, request):
        kw = request.POST.get('search', '')
        if kw:
            files = search(kw=kw)
            return render(request, 'index.html', {'files': files})
        else:
            return redirect('/')


def search(page=1, kw=''):
    if kw:
        file_list = Files.objects.filter(Q(name__contains=kw) | Q(desc__contains=kw))
    else:
        file_list = Files.objects.all()

    paginator = Paginator(file_list, 4)

    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return files

