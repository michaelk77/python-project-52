from django.urls import path

from .views import TasksView, TaskView, \
    CreateTask, TaskUpdate, TaskDelete


urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('<int:pk>/', TaskView.as_view(), name='task_show'),
    path('create/', CreateTask.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
]
