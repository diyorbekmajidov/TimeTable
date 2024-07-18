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

class ClassRoomScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoomScience
        fields = ['science', 'teacher', 'times_per_week']

    def validate(self, data):
        science = data['science']
        teacher = data['teacher']
        if not teacher.sciences.filter(id=science.id).exists():
            raise serializers.ValidationError(f'Teacher {teacher.fullname} does not teach {science.name}')
        return data

class ClassRoomSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    sciences = ClassRoomScienceSerializer(many=True)
    class Meta:
        model = ClassRoom
        fields = ['name', 'semina', 'leader', 'sciences']

    def get_teacher(self, obj):
        return obj.leader.fullname

    

