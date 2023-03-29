from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView
from task_manager.statuses.models import Status
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import AuthCheckMixin, \
    DeleteCheckMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses.forms import StatusForm


# Create your views here.


class StatusView(AuthCheckMixin, ListView):
    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}


class StatusCreate(AuthCheckMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status created successfully')
    extra_context = {'title': _('Create status'), 'button_text': _('Create')}


class StatusUpdate(AuthCheckMixin, SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully changed')
    extra_context = {'title': _('Change status'), 'button_text': _('Change')}


class StatusDelete(AuthCheckMixin, DeleteCheckMixin, SuccessMessageMixin,
                   DeleteView):
    template_name = 'statuses/del.html'
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    protected_message = _('This status is used in tasks')
    protected_url = reverse_lazy('statuses')
    extra_context = {'title': _('Delete status'),
                     'button_text': _('Yes, delete')}
