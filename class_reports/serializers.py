from rest_framework import serializers
from schedules.models import Period, Schedule
from teachers.models import Teacher
from .models import NonTeacherReport, Report


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'short_name']


class PeriodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'number', 'time_start', 'time_end']


class ScheduleInfoSerializer(serializers.ModelSerializer):
    schedule_class = serializers.StringRelatedField()
    schedule_course = serializers.StringRelatedField()
    schedule_time = serializers.StringRelatedField()
    teacher = TeacherNameSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'schedule_day', 'schedule_time', 'schedule_course', 'schedule_class', 'teacher']


class ReportSerializer(serializers.ModelSerializer):
    schedule = ScheduleInfoSerializer(read_only=True)
    schedule_id = serializers.PrimaryKeyRelatedField(
        queryset=Schedule.objects.all(), source='schedule', write_only=True
    )
    subtitute_teacher = TeacherNameSerializer(read_only=True, allow_null=True)
    subtitute_teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='subtitute_teacher', write_only=True, allow_null=True, required=False
    )
    reporter = TeacherNameSerializer(read_only=True, allow_null=True)
    reporter_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='reporter', write_only=True, allow_null=True, required=False
    )

    class Meta:
        model = Report
        fields = [
            'id', 'report_date', 'report_day', 'duty', 'notes', 'schedule', 'schedule_id',
            'status', 'subtitute_teacher', 'subtitute_teacher_id', 'reporter', 'reporter_id',
            'is_submitted', 'is_complete', 'semester', 'academic_year', 'type',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['report_day', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Check for duplicate reports for the same schedule on the same date.
        """
        if self.instance:  # This is an update
            return data

        report_date = data.get('report_date')
        schedule = data.get('schedule')

        if Report.objects.filter(report_date=report_date, schedule=schedule).exists():
            raise serializers.ValidationError("A report for this schedule on this date already exists.")
        return data


class NonTeacherReportSerializer(serializers.ModelSerializer):
    teacher = TeacherNameSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True
    )
    schedule_time = PeriodInfoSerializer(read_only=True)
    schedule_time_id = serializers.PrimaryKeyRelatedField(
        queryset=Period.objects.all(), source='schedule_time', write_only=True
    )

    class Meta:
        model = NonTeacherReport
        fields = [
            'id', 'teacher', 'teacher_id', 'report_date', 'report_day', 'schedule_time',
            'schedule_time_id', 'status', 'notes', 'is_submitted', 'is_complete',
            'semester', 'academic_year', 'type', 'created_at', 'updated_at'
        ]
        read_only_fields = ['report_day', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Check for duplicate reports for the same teacher at the same time on the same date.
        """
        if self.instance:  # This is an update
            return data

        report_date = data.get('report_date')
        teacher = data.get('teacher')
        schedule_time = data.get('schedule_time')

        if NonTeacherReport.objects.filter(
            report_date=report_date,
            teacher=teacher,
            schedule_time=schedule_time
        ).exists():
            raise serializers.ValidationError(
                "A non-teaching report for this teacher at this time on this date already exists."
            )
        return data