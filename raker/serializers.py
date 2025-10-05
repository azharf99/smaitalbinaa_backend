from rest_framework import serializers
from .models import LaporanPertanggungJawaban, ProgramKerja


class LaporanPertanggungJawabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaporanPertanggungJawaban
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ProgramKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramKerja
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']