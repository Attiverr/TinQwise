from django.urls import path
from .views import TodoCurrentList, TodoCompleteList, TodoUpdate, TodoComplete

urlpatterns = [
    path('todos/current', TodoCurrentList.as_view()),
    path('todos/completed', TodoCompleteList.as_view()),
    path('todos/<int:pk>', TodoUpdate.as_view()),
    path('todos/<int:pk>/complete', TodoComplete.as_view())
]
