from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import TaskList, TaskDetail, TaskCreate, upgrade_me, TaskUpdate
urlpatterns = [
    path('', TaskList.as_view()),
    path('<int:pk>', TaskDetail.as_view(), name='tasks'),
    path('create/', TaskCreate.as_view(), name='tasks_create'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name="update")
]