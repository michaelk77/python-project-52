from django.urls import path
from .views import Users, UserCrate, UserUpdate, UserDelete

urlpatterns = [
    path('', Users.as_view(), name='users'),
    path('create/', UserCrate.as_view(), name='sign_up'),
    path('<int:pk>/update/', UserUpdate.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDelete.as_view(), name='user_delete'),
]
