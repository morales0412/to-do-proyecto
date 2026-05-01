from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView,
)

from to_do_app.forms import TareaForm
from to_do_app.models import Tarea
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = "task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = "task_form.html"
    success_url = reverse_lazy("to_do_app:task_list")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "task_form.html"
    success_url = reverse_lazy("to_do_app:task_list")

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("to_do_app:task_list")

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)
