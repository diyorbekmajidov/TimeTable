from rest_framework import serializers

from .models import (Science, ClassRoom, ClassRoomScience)

class ScienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'


