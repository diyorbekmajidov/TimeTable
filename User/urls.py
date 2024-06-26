from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView


from .views import(
    RegisterUser,
    UserLoginAPIView,
    UserLogoutAPIView,
    GetUserAPIView
)

urlpatterns = [
    path('registeruser/', RegisterUser.as_view(), name='registration'),
    path('loginuser/', UserLoginAPIView.as_view(), name = 'loginview'),
    path('user/logout/', UserLogoutAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', GetUserAPIView.as_view(), name='get_user'),
]

