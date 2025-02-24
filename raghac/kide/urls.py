from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskCreateView.as_view()),
    path('tasks/<int:pk>', views.TaskDetailView.as_view()),
]
