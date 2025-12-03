from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer


# List all workouts or create a new one
class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# Retrieve, update, or delete a specific workout
class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
