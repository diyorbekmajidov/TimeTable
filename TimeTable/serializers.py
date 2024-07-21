from rest_framework import serializers

from .models import (Science, Teacher, ClassRoom, ClassRoomScience)

class ScienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'

class WorkdayField(serializers.Field):
    def to_representation(self, value):
        return value.split(',')

    def to_internal_value(self, data):
        if isinstance(data, list):
            return ','.join(data)
        raise serializers.ValidationError("Expected a list of strings.")

class TeacherSerializer(serializers.ModelSerializer):
    workdays = WorkdayField()

    class Meta:
        model = Teacher
        fields = ['fullname', 'sciences', 'workdays', 'description']

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

    

