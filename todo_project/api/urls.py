from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>', views.taskDelete, name='task-delete'),
    path('folder-list/', views.folderList, name='folder-list'),
    path('folder-detail/<str:pk>/', views.folderDetail, name='folder-detail'),
    path('folder-create/', views.folderCreate, name='folder-create'),
    path('folder-update/<str:pk>', views.folderUpdate, name='folder-update'),
    path('folder-delete/<str:pk>', views.folderDelete, name='folder-delete'),
]