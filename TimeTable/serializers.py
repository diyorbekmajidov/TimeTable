from rest_framework import serializers

from .models import (Science, Teacher, ClassRoom, ClassRoomScience)

class ScienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['name', 'semina', 'leader', 'sciences']

