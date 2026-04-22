from django.shortcuts import render
from to_do_app.models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"


class TaskDetailView(ListView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"


# Create your views here.
