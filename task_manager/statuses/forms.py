from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=150, required=True)

    class Meta:
        model = Status
        fields = ('name',)
