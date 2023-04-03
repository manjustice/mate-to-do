from django.shortcuts import render
from django.views import generic

from.models import Tag, Task


def index(request, *args, **kwargs):
    return render(request, "index.html")


class TagListView(generic.ListView):
    model = Tag
