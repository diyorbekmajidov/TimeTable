from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (UserSerializer,UserLoginSerializer)
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class RegisterUser(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        data = request.data
        data['password'] = make_password(request.data['password'])
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
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)

	def post(self, request):
		phone_number = request.data.get('phone_number', None)
		user_password = request.data.get('password', None)
		if not user_password:
			raise AuthenticationFailed('A user password is needed.')

		if not phone_number:
			raise AuthenticationFailed('An user email is needed.')

		user_instance = authenticate(phone_number=phone_number, password=user_password)

		if not user_instance:
			raise AuthenticationFailed('User not found.')

		if user_instance.is_active:
			refresh =  RefreshToken.for_user(user_instance)
			response = Response()
			response.set_cookie(key='access_token', value=str(refresh.access_token), httponly=True)
			response.data = {
				'access_token': str(refresh.access_token)
			}
			return response

		return Response({
			'message': 'Something went wrong.'
		})


# class UserViewAPI(APIView):
# 	authentication_classes = (TokenAuthentication,)
# 	permission_classes = (AllowAny,)

# 	def get(self, request):
# 		user_token = request.COOKIES.get('access_token')

# 		if not user_token:
# 			raise AuthenticationFailed('Unauthenticated user.')

# 		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

# 		user_model = get_user_model()
# 		user = user_model.objects.filter(user_id=payload['user_id']).first()
# 		user_serializer = UserRegistrationSerializer(user)
# 		return Response(user_serializer.data)



class UserLogoutViewAPI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (AllowAny,)

	def get(self, request):
		user_token = request.COOKIES.get('access_token', None)
		if user_token:
			response = Response()
			response.delete_cookie('access_token')
			response.data = {
				'message': 'Logged out successfully.'
			}
			return response
		response = Response()
		response.data = {
			'message': 'User is already logged out.'
		}
		return response
            
