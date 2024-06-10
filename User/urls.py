from django.urls import path, include


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
    path('user/', GetUserAPIView.as_view(), name='get_user'),
]

