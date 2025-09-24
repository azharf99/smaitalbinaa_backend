from rest_framework import serializers
from .models import AcademicCalendar

class AcademicCalendarSerializer(serializers.ModelSerializer):
    """
    Serializer for the AcademicCalendar model.

    This serializer converts the AcademicCalendar model instances into JSON format
    and validates the data for creating and updating instances.
    """
    class Meta:
        model = AcademicCalendar
        fields = '__all__' # This will include all fields from the model in the API
