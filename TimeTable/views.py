from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from .serializers import (ScienceSerializers)
from .models import Science


class ScienceViewsets(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    serializer_class = ScienceSerializers
    queryset = Science.objects.all()

    
    def post(self, request):
        serializers = ScienceSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        print(serializers.errors)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
