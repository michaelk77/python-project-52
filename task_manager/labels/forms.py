from task_manager.labels.models import Label
from django import forms
from django.utils.translation import gettext_lazy as _


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, required=True, label=_("Name")
    )

    class Meta:
        model = Label
        fields = ('name',)
