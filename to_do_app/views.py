from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from to_do_app.forms import TareaForm
from to_do_app.models import Tarea


class TaskListView(ListView):
    model = Tarea
    template_name = "task_list.html"
    context_object_name = "tasks"


class TaskDetailView(ListView):
    model = Tarea
    template_name = "task_detail.html"
    context_object_name = "task"
    success_url = reverse_lazy("task_list")


class TaskCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Tarea
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task_list")
