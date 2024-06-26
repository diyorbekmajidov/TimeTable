from django.urls import path, include
from rest_framework import routers
from .views import (ScienceApiViews, ScienceApiviewById, TeacherApiView, TeacherApiViewById)

# router = routers.DefaultRouter()
# router.register(r'custom-viewset', ScienceViewsets)
urlpatterns = [
    path('science/', ScienceApiViews.as_view()),
    path('science/<int:pk>/', ScienceApiviewById.as_view()),
    path('teacher/', TeacherApiView.as_view()),
    path('teacher/<int:pk>/', TeacherApiViewById.as_view()),
]
