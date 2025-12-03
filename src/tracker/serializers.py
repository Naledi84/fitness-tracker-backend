from rest_framework import serializers
from .models import Workout, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'height', 'weight', 'goal']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'date', 'duration', 'calories_burned']
