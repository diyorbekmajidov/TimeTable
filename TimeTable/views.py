from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ScienceSerializers, TeacherSerializer, ClassRoomSerializer
from .models import Science, Teacher, ClassRoom
from django.shortcuts import render, redirect
from .models import Teacher


from django.views import View

class ScienceIsGroup(View):
    def get(self, request):
        science_id = request.GET.get('id')
        try:
            science = Science.objects.get(pk=science_id)
            is_group = science.is_group
            return JsonResponse({'is_group': is_group})
        except Science.DoesNotExist:
            return JsonResponse({'error': 'Science not found'}, status=404)


class ScienceApiViews(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    serializer_class = ScienceSerializers
    queryset = Science.objects.all()

    @swagger_auto_schema(
        operation_summary="Create a new science entry",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Science name'),
                'is_group' : openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Science is group'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Science description'),
            },
            required=['name'],  # Specify required fields as a list of property names
        ),
        responses={
            201: openapi.Response('Created', ScienceSerializers),
            400: "Bad Request"
        },
        security=[{'Bearer': []}]  # Apply the security scheme
    )

    def post(self, request):
        serializers = ScienceSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="List all sciences",
        responses={
            200: openapi.Response('OK', ScienceSerializers(many=True)),
        }
    )
    def get(self, request):
        science = Science.objects.all()
        serializer = ScienceSerializers(science, many=True)
        return Response(serializer.data)


class ScienceApiviewById(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    serializer_class = ScienceSerializers
    queryset = Science.objects.all()

    @swagger_auto_schema(
        operation_summary="Retrieve a science by ID",
        responses={
            200: openapi.Response('OK', ScienceSerializers),
            404: "Not Found"
        }
    )
    def get(self, request, pk):
        try:
            science = Science.objects.get(id=pk)
            serializer = ScienceSerializers(science)
            return Response(serializer.data)
        except Science.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

class TeacherApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    @swagger_auto_schema(
        operation_summary="Creat a new teacher here",
        responses={
            200: openapi.Response('OK', TeacherSerializer),
            404: "Not Found"
        }
    )
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
class TeacherApiViewById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    @swagger_auto_schema(
        operation_summary="Retrieve a teacher by ID",
        responses={
            200: openapi.Response('OK', TeacherSerializer),
            404: "Not Found"
        }
    )
    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ClassRoomApiView(APIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]
    serializer_class = ClassRoomSerializer

    def post(self, request):
        serializer = ClassRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        science = ClassRoom.objects.all()
        serializer = ScienceSerializers(science, many=True)
        return Response(serializer.data)
    