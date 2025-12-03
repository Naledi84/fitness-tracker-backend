from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
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

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    date = models.DateField()
    duration = models.IntegerField()  # minutes
    calories_burned = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"


