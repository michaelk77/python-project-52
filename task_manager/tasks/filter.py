from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task
from ..labels.models import Label


class TaskFilter(FilterSet):
    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label')
    )

    own_tasks = BooleanFilter(
        label=_('Only own tasks'),
        widget=forms.CheckboxInput,
        method='get_own_tasks',
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']

    def get_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
