from rest_framework import serializers
from .models import CustomUser

from django.contrib.auth import get_user_model, authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if not phone_number or not password:
            raise serializers.ValidationError("Telefon raqami va parol talab qilinadi.")
        
        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError("Telefon raqami yoki parol noto\‘g\‘ri.")
        
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faol emas.")
        
        data['user'] = user
        return data