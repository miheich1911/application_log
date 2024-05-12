from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView
from .filters import TaskFilter
from .forms import TaskForm, TaskUpdateForm
from .models import Task


class TaskList(ListView):
    model = Task
    ordering = '-time_in'
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TaskFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['is_not_executors'] = not self.request.user.groups.filter(name='executors').exists()
        return context


class TaskDetail(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_executors'] = self.request.user.groups.filter(name='executors').exists()
        return context

    def form_valid(self, form):
        form.instance.executor = self.request.user.username
        return super(TaskUpdate, self).form_valid(form)


class TaskCreate(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    model = Task
    template_name = 'task_edit.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(TaskCreate, self).form_valid(form)


@login_required
def upgrade_me(request):
    user = request.user
    executors_group = Group.objects.get(name='executors')
    if not request.user.groups.filter(name='executors').exists():
        executors_group.user_set.add(user)
    return redirect('/')





