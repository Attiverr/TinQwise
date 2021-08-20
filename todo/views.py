from django.utils import timezone
from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoCurrentSerializer, TodoUpdateSerializer, TodoCompleteSerializer


class TodoCurrentList(generics.ListCreateAPIView):
    serializer_class = TodoCurrentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user_id=user, complete_data__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class TodoCompleteList(generics.ListAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user_id=user, complete_data__isnull=False)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class TodoUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoCurrentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user_id=user)


class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user_id=user, complete_data__isnull=True)

    def perform_update(self, serializer):
        serializer.instance.complete_data = timezone.now()
        serializer.save()
