from task_manager.statuses import views
from django.urls import path

urlpatterns = [
    path('', views.StatusView.as_view(), name='statuses'),
    path('create/', views.StatusCreate.as_view(), name='status_create'),
    path('<int:pk>/update/', views.StatusUpdate.as_view(),
         name='status_update'),
    path('<int:pk>/delete/', views.StatusDelete.as_view(),
         name='status_delete'),
]
