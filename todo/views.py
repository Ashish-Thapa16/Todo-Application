from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Task
from .form import TaskForm


class TaskListView(ListView) :
    model = Task
    template_name = "base.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView) :
    model = Task
    form_class = TaskForm
    template_name = "create_task.html"
    success_url = "/"

class TaskDeleteView(DeleteView) :
    model = Task
    template_name = "task_confirm_delete.html"
    context_object_name = "object"
    success_url = "/"