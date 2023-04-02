from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.form import UserForm
from task_manager.mixins import UserPermissionCheckMixin, AuthCheckMixin, \
    DeleteCheckMixin


class Users(ListView):
    model = User
    template_name = 'users/all.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users')}


class UserCrate(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User created successfully')
    extra_context = {'title': _('Create user'), 'button_text': _('Register')}


class UserUpdate(AuthCheckMixin, SuccessMessageMixin, UserPermissionCheckMixin,
                 UpdateView):
    model = User
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = _('User updated successfully')
    permission_url = reverse_lazy('users')
    permission_message = _('You do not have permission to update this user')
    extra_context = {'title': _('Update user'), 'button_text': _('Update')}


class UserDelete(AuthCheckMixin, UserPermissionCheckMixin,
                 DeleteCheckMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('home')
    success_message = _('User is successfully deleted')
    permission_url = reverse_lazy('users')
    protected_url = reverse_lazy('users')
    permission_message = _('You not have permission to delete this user')
    protected_message = _('This user have project and cannot be deleted')
    extra_context = {'title': _('Delete user'), 'button_text': _('Yes, delete')}
