from rest_framework import serializers
from classes.models import Class
from courses.models import Course, Subject
from teachers.models import Teacher
from .models import Period, ReporterSchedule, Schedule


class SubjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name']


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name']


class CourseNameSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    course = SubjectNameSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course', write_only=True
    )


    class Meta:
        model = Course
        fields = ['id', 'course', 'course_id', 'teacher']


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = [
            'id', 'number', 'time_start', 'short_time_start', 'time_end',
            'short_time_end', 'type', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class ScheduleSerializer(serializers.ModelSerializer):
    schedule_time = PeriodSerializer(read_only=True)
    schedule_time_id = serializers.PrimaryKeyRelatedField(
        queryset=Period.objects.all(), source='schedule_time', write_only=True
    )
    schedule_course = CourseNameSerializer(read_only=True)
    schedule_course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='schedule_course', write_only=True
    )
    schedule_class = ClassNameSerializer(read_only=True)
    schedule_class_id = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(), source='schedule_class', write_only=True
    )
    teacher = TeacherNameSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = [
            'id', 'schedule_day', 'schedule_time', 'schedule_time_id',
            'schedule_course', 'schedule_course_id', 'schedule_class',
            'schedule_class_id', 'teacher', 'semester', 'academic_year', 'type',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['teacher', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Check that a teacher is not scheduled for the same time slot twice.
        """
        schedule_day = data.get('schedule_day')
        schedule_time = data.get('schedule_time')
        schedule_course = data.get('schedule_course')


        if not all([schedule_day, schedule_time, schedule_course]):
            return data # Let default validation handle missing fields

        teacher = schedule_course.teacher

        # Check for existing schedules for the same teacher at the same time
        existing_schedule, is_created = Schedule.objects.get_or_create(
            schedule_day=schedule_day,
            schedule_time=schedule_time,
            schedule_course=schedule_course,
            defaults=data
        )

        if not is_created:
            raise serializers.ValidationError(f"Teacher {teacher.teacher_name} is already scheduled at this time.")

        return data


class ReporterScheduleSerializer(serializers.ModelSerializer):
    reporter = TeacherNameSerializer(read_only=True)
    reporter_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='reporter', write_only=True
    )

    class Meta:
        model = ReporterSchedule
        fields = [
            'id', 'schedule_day', 'schedule_time', 'reporter', 'reporter_id',
            'time_start', 'time_end', 'semester', 'academic_year', 'type',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']