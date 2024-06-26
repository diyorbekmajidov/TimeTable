from django.urls import path, include
from rest_framework import routers
from .views import (ScienceViewsets,)

# router = routers.DefaultRouter()
# router.register(r'custom-viewset', ScienceViewsets)
urlpatterns = [
    path('science/', ScienceViewsets.as_view()),
]
