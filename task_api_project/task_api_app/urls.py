from django.urls import path
from .views import TaskListCreateApiView, TaskRetrieveUpdateDestroyApiView, CommentApiView


urlpatterns = [
    path('tasks/', TaskListCreateApiView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyApiView.as_view(), name='task_detail'),
    path('comments/', CommentApiView.as_view(), name='comment_create'),
]