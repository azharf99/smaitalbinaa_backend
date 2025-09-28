from django.utils import timezone
from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher
from .models import Tahfidz, Target, Tilawah
from students.serializers import StudentSerializer
from teachers.serializers import TeacherSerializer

class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']

class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']

class TahfidzSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tahfidz model.
    """
    santri = StudentNameSerializer(read_only=True)
    pembimbing = TeacherNameSerializer(read_only=True)

    santri_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.select_related('student_class').filter(student_status="Aktif"), source='santri', write_only=True
    )
    pembimbing_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='pembimbing', write_only=True
    )

    class Meta:
        model = Tahfidz
        fields = [
            'id', 'santri', 'pembimbing', 'pembimbing_id', 'hafalan', 'pencapaian_sebelumnya',
            'pencapaian_sekarang', 'catatan', 'semester', 'academic_year', 'santri_id'
        ]


class TargetSerializer(serializers.ModelSerializer):
    """
    Serializer for the Target model.
    """
    class Meta:
        model = Target
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TargetTilawahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'tanggal', 'halaman', 'nomor_surat', 'nama_surat', 'ayat']

class TilawahSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tilawah model.
    """
    # santri = StudentSerializer(read_only=True)
    # santri_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Tilawah.santri.get_queryset().filter(student_status="Aktif"),
    #     source='santri',
    #     write_only=True
    # )
    # target_tilawah = TargetSerializer(read_only=True)
    # target_tilawah_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Target.objects.filter(tanggal__lte=timezone.now().date()),
    #     source='target_tilawah',
    #     write_only=True,
    #     allow_null=True
    # )
    # pendamping = TeacherSerializer(many=True, read_only=True)
    # pendamping_ids = serializers.PrimaryKeyRelatedField(
    #     queryset=Teacher.objects.filter(status="Aktif", gender="L"),
    #     source='pendamping',
    #     write_only=True,
    #     many=True
    # )

    santri = StudentNameSerializer(read_only=True)
    pendamping = TeacherNameSerializer(many=True, read_only=True)
    target_tilawah = TargetTilawahSerializer(read_only=True)

    # Use PrimaryKeyRelatedField for write operations (for creating/updating)
    santri_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='santri', write_only=True
    )
    pendamping_ids = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='pendamping', many=True, write_only=True
    )
    target_tilawah_id = serializers.PrimaryKeyRelatedField(
        queryset=Target.objects.all(), source='target_tilawah', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Tilawah
        fields = '__all__'
        read_only_fields = ['tercapai', 'created_at', 'updated_at']


class StudentTilawahDataSerializer(serializers.Serializer):

    """Serializer for individual student data within the quick create form."""
    santri_id = serializers.IntegerField()
    kehadiran = serializers.CharField(max_length=10)
    halaman = serializers.IntegerField(allow_null=True, required=False)
    surat = serializers.IntegerField(allow_null=True, required=False)
    ayat = serializers.IntegerField(allow_null=True, required=False)
    kelancaran = serializers.CharField(max_length=20, allow_null=True, required=False)
    tajwid = serializers.CharField(max_length=20, allow_null=True, required=False)


class QuickTilawahCreateSerializer(serializers.Serializer):

    """
    Serializer for handling bulk creation of Tilawah records from the quick create form.
    """
    tanggal = serializers.DateField()
    catatan = serializers.CharField(max_length=255, allow_blank=True, required=False)
    pendamping_ids = serializers.ListField(child=serializers.IntegerField())
    student_data = serializers.ListField(child=StudentTilawahDataSerializer())