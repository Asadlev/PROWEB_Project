from rest_framework import serializers
from .models import Task, Comment
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            '__all__'
        ]

    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError('Скрок оплаты не может быть перенесен в прошлое')

        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'task',
            'text',
            'created_at',
        ]


