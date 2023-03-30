# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, \
    DeleteView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView
from task_manager.mixins import AuthCheckMixin, AuthorDeletion
from task_manager.tasks.filter import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TasksView(AuthCheckMixin, FilterView):
    template_name = 'tasks/list.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {'title': _('Tasks'), 'button_text': _('Show'), }


class TaskView(AuthCheckMixin, DetailView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'title': _('Task preview')
    }


class CreateTask(AuthCheckMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task created successfully!')
    extra_context = {'title': _('Create task'), 'button_text': _('Create')}

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdate(AuthCheckMixin, SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')
    extra_context = {
        'title': _('Task change'),
        'button_text': _('Change'),
    }


class TaskDelete(AuthCheckMixin, AuthorDeletion,
                 SuccessMessageMixin, DeleteView):
    template_name = 'tasks/del.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    author_message = _('The task can be deleted only by its author')
    author_url = reverse_lazy('tasks')
    extra_context = {
        'title': _('Delete task'),
        'button_text': _('Yes, delete'),
    }
