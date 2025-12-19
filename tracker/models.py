from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)   # cm or meters
    weight = models.FloatField(null=True, blank=True)   # kg
    goal = models.CharField(max_length=255, null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="tracker_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="tracker_user_set",
        blank=True
    )

    def __str__(self):
        return self.username


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    date = models.DateField()
    duration = models.PositiveIntegerField()  # minutes
    calories_burned = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"





