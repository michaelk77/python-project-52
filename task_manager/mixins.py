from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _


class DeleteCheckMixin:
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)

        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class AuthCheckMixin(LoginRequiredMixin):
    auth_message = _('You are not logged in! Please log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


class UserPermissionCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)


class AuthorDeletion(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.author_message)
        return redirect(self.author_url)


class Deletion:
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
