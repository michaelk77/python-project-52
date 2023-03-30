from django.urls import path

from task_manager.labels.views import Labels, LabelCreate,\
    LabelUpdate, LabelDelete


urlpatterns = [
    path('', Labels.as_view(), name='labels'),
    path('create/', LabelCreate.as_view(), name='label_create'),
    path('<int:pk>/update/', LabelUpdate.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDelete.as_view(), name='label_delete'),
]
