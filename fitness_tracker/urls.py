"""
URL configuration for fitness_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Simple root view to avoid Bad Request (400) at /
def home(request):
    return JsonResponse({"message": "Fitness Tracker API is running!"})

urlpatterns = [
    path("", home, name="home"),                # Root endpoint
    path("admin/", admin.site.urls),            # Django admin
    path("api/", include("tracker.urls")),      # Include tracker app routes
]


