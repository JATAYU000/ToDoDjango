from django.urls import path
from .views import TaskListView,TaskDetailView,TaskDeleteView,TaskCreateView,TaskUpdateView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(),name='main-page'),
    path('login/', views.login,name='login-page'),
    path('register/',views.register,name='register-page'),
    path('item/<int:pk>/', TaskDetailView.as_view(),name='task-detail'),
    path('item/new/', TaskCreateView.as_view(),name='task-create'),
    path('item/<int:pk>/update/', TaskUpdateView.as_view(),name='task-update'),
    path('item/<int:pk>/delete/', TaskDeleteView.as_view(),name='task-delete'),

]
