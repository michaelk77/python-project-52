from django.db import models

# Create your models here.

from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name=_('Name'))

    description = models.TextField(max_length=10000,
                                   verbose_name=_('Description'))
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_('Creation date'))

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='author',
                               verbose_name=_('Author'))

    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               related_name='statuses',
                               verbose_name=_('Status'))

    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='executor',
                                 verbose_name=_('Executor'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')


class TaskStatus(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name='task')
