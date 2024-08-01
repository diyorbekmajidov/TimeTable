from django.urls import path, include
from rest_framework import routers
from django.views.i18n import set_language
from .views import (ScienceApiViews, ScienceApiviewById, TeacherApiView, TeacherApiViewById,
                    ClassRoomApiView, ScienceIsGroup)

# router = routers.DefaultRouter()
# router.register(r'custom-viewset', ScienceViewsets)
urlpatterns = [
    path('i18n/', set_language, name='set_language'),
    path('science/', ScienceApiViews.as_view()),
    path('science/<int:pk>/', ScienceApiviewById.as_view()),
    path('teacher/', TeacherApiView.as_view()),
    path('teacher/<int:pk>/', TeacherApiViewById.as_view()),
    path('classroom/', ClassRoomApiView.as_view()),
    path('science/is/group/', ScienceIsGroup.as_view())
]
