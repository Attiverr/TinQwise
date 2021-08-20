from django.utils import timezone
from rest_framework import serializers
from .models import Todo


class TodoCompleteSerializer(serializers.ModelSerializer):
    days_after_complete = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source='user_id.username')
    complete_data = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ["id", "title", "complete_data", "user_id", "days_after_complete"]

    def get_days_after_complete(self, todo):
        if todo.complete_data:
            result = (timezone.now() - todo.complete_data).days
        else:
            result = None
        return result


class TodoCurrentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Todo
        read_only_fields = ["complete_data"]
        fields = ["id", "title", "complete_data", "user_id"]


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ["title", "complete_data", "user_id"]
        fields = ["id"]
