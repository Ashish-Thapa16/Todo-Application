from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name = "list-task"),
    path("create/", TaskCreateView.as_view(), name = "create-task"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name = "delete-task"),
]