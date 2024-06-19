from rest_framework import serializers
from .models import CustomUser
from .validators import validate_password


from django.contrib.auth import  authenticate

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'password', 'password2', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Parol maydonlari mos kelmadi."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user

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
            raise serializers.ValidationError("Telefon raqami yoki parol noto‘g‘ri.")
        
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faol emas.")
        
        data['user'] = user
        return data