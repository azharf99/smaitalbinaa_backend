from rest_framework import serializers
from students.models import Student
from teachers.models import Teacher
from .models import Subject, Group, Private


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name']


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class SubjectSerializer(serializers.ModelSerializer):
    pembimbing = TeacherNameSerializer(many=True, read_only=True)
    pembimbing_ids = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='pembimbing',
        write_only=True,
        many=True,
        required=False
    )

    class Meta:
        model = Subject
        fields = ['id', 'nama_pelajaran', 'pembimbing', 'pembimbing_ids', 'created_at', 'updated_at']


class GroupSerializer(serializers.ModelSerializer):
    pelajaran = SubjectSerializer(read_only=True)
    pelajaran_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source='pelajaran', write_only=True
    )
    santri = StudentNameSerializer(many=True, read_only=True)
    santri_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='santri', write_only=True, many=True, required=False
    )

    class Meta:
        model = Group
        fields = [
            'id', 'nama_kelompok', 'jenis_kelompok', 'pelajaran', 'pelajaran_id',
            'jadwal', 'waktu', 'santri', 'santri_ids', 'created_at', 'updated_at'
        ]


class PrivateSerializer(serializers.ModelSerializer):
    pembimbing = TeacherNameSerializer(read_only=True)
    pembimbing_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='pembimbing', write_only=True
    )
    pelajaran = SubjectSerializer(read_only=True)
    pelajaran_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source='pelajaran', write_only=True
    )
    kelompok = GroupSerializer(read_only=True)
    kelompok_id = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), source='kelompok', write_only=True, allow_null=True, required=False
    )
    kehadiran_santri = StudentNameSerializer(many=True, read_only=True)
    kehadiran_santri_ids = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='kehadiran_santri', write_only=True, many=True
    )

    class Meta:
        model = Private
        fields = [
            'id', 'pembimbing', 'pembimbing_id', 'pelajaran', 'pelajaran_id',
            'tanggal_bimbingan', 'waktu_bimbingan', 'catatan_bimbingan', 'kelompok', 'kelompok_id',
            'kehadiran_santri', 'kehadiran_santri_ids', 'foto', 'semester', 'tahun_ajaran'
        ]
        read_only_fields = ['created_at', 'updated_at']