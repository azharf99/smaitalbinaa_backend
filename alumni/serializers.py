from rest_framework import serializers
from .models import Alumni

class AlumniSerializer(serializers.ModelSerializer):
    """
    Serializer for the Alumni model.
    """
    class Meta:
        model = Alumni
        fields = [
            'id', 'nis', 'nisn', 'name', 'group', 'birth_place', 'birth_date',
            'gender', 'address', 'city', 'province', 'state', 'phone',
            'last_class', 'graduate_year', 'undergraduate_department',
            'undergraduate_university', 'undergraduate_university_entrance',
            'postgraduate_department', 'postgraduate_university',
            'postgraduate_university_entrance', 'doctoral_department',
            'doctoral_university', 'doctoral_university_entrance', 'job',
            'company_name', 'married', 'father_name', 'mother_name',
            'family_phone', 'photo', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']