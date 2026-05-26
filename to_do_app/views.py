from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from to_do_app.forms import TareaForm
from to_do_app.models import Tarea
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user).order_by(
            "completada", "-fecha_creacion"
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        total = qs.count()
        completed = qs.filter(completada=True).count()
        ctx["total"] = total
        ctx["completed"] = completed
        ctx["pending"] = total - completed
        ctx["completion_pct"] = int(completed / total * 100) if total else 0
        return ctx


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
    template_name = "task_update.html"
    success_url = reverse_lazy("to_do_app:task_list")

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("to_do_app:task_list")

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)


class TaskToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        tarea.completada = not tarea.completada
        tarea.save()
        return HttpResponseRedirect(reverse("to_do_app:task_list"))
