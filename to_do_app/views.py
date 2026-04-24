from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from to_do_app.forms import TareaForm
from to_do_app.models import Tarea


class TaskListView(ListView):
    model = Tarea
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TareaForm()
        return context


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
