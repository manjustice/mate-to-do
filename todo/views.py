from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task
from .forms import TagForm, TaskForm


def index(request, *args, **kwargs):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "todo/index.html", context=context)


def update_is_done(request, pk=None):
    if request.method == "POST" and pk is not None:
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
    return redirect("todo:index")


class TagListView(generic.ListView):
    model = Tag


class CreateTaskView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class UpdateTaskView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class CreateTagView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags")


class UpdateTagView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags")


class DeleteTagView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags")
