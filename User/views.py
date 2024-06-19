from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (UserSerializer,UserLoginSerializer)
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterUser(APIView):
    permission_classes = (AllowAny,)
    @swagger_auto_schema(request_body=UserSerializer)

    def post(self, request):
        data = request.data
        # data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            if user :
                refresh = RefreshToken.for_user(user)
                data = {'refresh': str(refresh),'access': str(refresh.access_token)}
                response = Response(data, status=status.HTTP_201_CREATED)
                response.set_cookie(key='access_token', value=str(refresh.access_token))
                return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            response = Response()
            response.set_cookie(key='access_token', value=str(refresh.access_token), httponly=True)
            response.data = {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('refresh_token', openapi.IN_QUERY, description="Refresh Token", type=openapi.TYPE_STRING)]
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response(status=status.HTTP_205_RESET_CONTENT)
            response.delete_cookie('access_token')
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
     



class GetUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(responses={200: UserSerializer})

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
