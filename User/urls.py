from django.urls import path, include

from .views import(
    RegisterUser,
    UserLoginAPIView,
    UserLogoutViewAPI
)

urlpatterns = [
    path('registeruser/', RegisterUser.as_view(), name='registration'),
    path('loginuser/', UserLoginAPIView.as_view(), name = 'loginview'),
    path('user/logout/', UserLogoutViewAPI.as_view()),
]
