from rest_framework import serializers
from .models import Prestasi, ProgramPrestasi

class PrestasiSerializer(serializers.ModelSerializer):
    """
    Serializer for the Prestasi model.
    """
    class Meta:
        model = Prestasi
        fields = '__all__'


class ProgramPrestasiSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProgramPrestasi model.
    """
    class Meta:
        model = ProgramPrestasi
        fields = '__all__'