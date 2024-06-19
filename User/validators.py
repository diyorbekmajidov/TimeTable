# validators.py
import re
from rest_framework import serializers

def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError('Parol kamida 8 ta belgidan iborat bo\'lishi kerak.')
    if not re.search(r'[A-Za-z]', value):
        raise serializers.ValidationError('Parolda kamida bitta harf bo\'lishi kerak.')
    return value
