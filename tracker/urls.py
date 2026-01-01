from django.urls import path
from .views import (
    WorkoutListCreateView,
    WorkoutDetailView,
    RegisterView,
    LoginView,
    ActivityMetricsView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),

    # Workout CRUD
    path("workouts/", WorkoutListCreateView.as_view(), name="workout-list"),
    path("workouts/<int:pk>/", WorkoutDetailView.as_view(), name="workout-detail"),

    # Metrics (totals, weekly, daily)
    path("metrics/", ActivityMetricsView.as_view(), name="activity-metrics"),
]
