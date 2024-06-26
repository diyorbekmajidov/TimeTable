from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ScienceSerializers, TeacherSerializers
from .models import Science, Teacher


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
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Science description'),
            },
            required=['name'],  # Specify required fields as a list of property names
        ),
        responses={
            201: openapi.Response('Created', ScienceSerializers),
            400: "Bad Request"
        }
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
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

    @swagger_auto_schema(
        operation_summary="Create a new teacher entry",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'fullname': openapi.Schema(type=openapi.TYPE_STRING, description='Teacher full name'),
                'science': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='List of science IDs'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Teacher description'),
            },
            required=['fullname', 'science']
        ),
        responses={
            201: openapi.Response('Created', TeacherSerializers),
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializers = TeacherSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="List all teachers",
        responses={
            200: openapi.Response('OK', TeacherSerializers(many=True)),
        }
    )
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializers(teacher, many=True)
        return Response(serializer.data)
    
class TeacherApiViewById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()

    @swagger_auto_schema(
        operation_summary="Retrieve a teacher by ID",
        responses={
            200: openapi.Response('OK', TeacherSerializers),
            404: "Not Found"
        }
    )
    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            serializer = TeacherSerializers(teacher)
            return Response(serializer.data)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
