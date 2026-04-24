from django.shortcuts import render
from to_do_app.models import Tarea
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Tarea
    template_name = "task_list.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("task_list")


class TaskDetailView(ListView):
    model = Tarea
    template_name = "task_detail.html"
    context_object_name = "task"
    success_url = reverse_lazy("task_list")
