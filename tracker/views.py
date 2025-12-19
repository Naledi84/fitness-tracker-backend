from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Sum, Avg
from django.db.models.functions import TruncWeek, TruncDay

from .models import Workout, User
from .serializers import WorkoutSerializer, RegisterSerializer


class WorkoutListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {"access": str(refresh.access_token)},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {"access": str(refresh.access_token)},
            status=status.HTTP_200_OK
        )


class ActivityMetricsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        workouts = Workout.objects.filter(user=request.user)

        # Overall totals
        totals = workouts.aggregate(
            total_duration=Sum("duration"),
            total_calories=Sum("calories_burned"),
            avg_duration=Avg("duration"),
            avg_calories=Avg("calories_burned"),
        )

        # Weekly breakdown
        weekly_qs = (
            workouts
            .annotate(week_start=TruncWeek("date"))
            .values("week_start")
            .annotate(
                weekly_duration=Sum("duration"),
                weekly_calories=Sum("calories_burned"),
                avg_weekly_duration=Avg("duration"),
                avg_weekly_calories=Avg("calories_burned"),
            )
            .order_by("week_start")
        )
        weekly = [
            {
                "week_start": item["week_start"],
                "weekly_duration": item["weekly_duration"] or 0,
                "weekly_calories": item["weekly_calories"] or 0,
                "avg_weekly_duration": round(item["avg_weekly_duration"] or 0, 2),
                "avg_weekly_calories": round(item["avg_weekly_calories"] or 0, 2),
            }
            for item in weekly_qs
        ]

        # Daily breakdown
        daily_qs = (
            workouts
            .annotate(day=TruncDay("date"))
            .values("day")
            .annotate(
                daily_duration=Sum("duration"),
                daily_calories=Sum("calories_burned"),
            )
            .order_by("day")
        )
        daily = [
            {
                "day": item["day"],
                "daily_duration": item["daily_duration"] or 0,
                "daily_calories": item["daily_calories"] or 0,
            }
            for item in daily_qs
        ]

        return Response({
            "totals": {
                "total_duration": totals["total_duration"] or 0,
                "total_calories": totals["total_calories"] or 0,
                "avg_duration": round(totals["avg_duration"] or 0, 2),
                "avg_calories": round(totals["avg_calories"] or 0, 2),
            },
            "weekly": weekly,
            "daily": daily,
        })







