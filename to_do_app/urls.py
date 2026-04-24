from django.urls import path

from to_do_app.views import TaskCreateView, TaskDetailView, TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
]
