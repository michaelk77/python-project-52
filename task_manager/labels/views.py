from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.mixins import AuthCheckMixin, Deletion


# Create your views here.


class Labels(AuthCheckMixin, ListView):
    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'
    extra_context = {'title': _('Labels')}


class LabelCreate(AuthCheckMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdate(AuthCheckMixin, SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully changed')
    extra_context = {
        'title': _('Label change'),
        'button_text': _('Change'),
    }


class LabelDelete(AuthCheckMixin, SuccessMessageMixin, Deletion,
                  DeleteView):
    template_name = 'labels/del.html'
    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    extra_context = {
        'title': _('Label delete'),
        'button_text': _('Yes, delete'),
    }
