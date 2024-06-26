from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (ScienceSerializers, TeacherSerializers)
from .models import (Science, Teacher)


class ScienceApiViews(APIView):
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
    
    def get(self, request):
        science = Science.objects.all()
        serializer = ScienceSerializers(science, many=True)
        return Response(serializer.data)
    

class ScienceApiviewById(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    serializer_class = ScienceSerializers
    queryset = Science.objects.all()

    def get(self, request, pk):
        science = Science.objects.get(id=pk)
        serializer = ScienceSerializers(science)
        return Response(serializer.data)
    
    

class TeacherApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

    def post( self, request):
        serializers = TeacherSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializers(teacher, many=True)
        return Response(serializer.data)
    
class TeacherApiViewById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

    def get(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherSerializers(teacher)
        return Response(serializer.data)
    

