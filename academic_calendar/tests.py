from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import AcademicCalendar
from .serializers import AcademicCalendarSerializer
import datetime

class AcademicCalendarAPITests(APITestCase):
    """
    Tests for the AcademicCalendar API.
    """
    def setUp(self):
        """
        Set up initial data for tests.
        """
        self.event1 = AcademicCalendar.objects.create(
            event_name="School Year Start",
            event_start_date=datetime.date(2025, 9, 1),
            event_end_date=datetime.date(2025, 9, 1),
            description="First day of the school year.",
            category="Academic",
            type="Putra"
        )
        self.event2 = AcademicCalendar.objects.create(
            event_name="Mid-term Exams",
            event_start_date=datetime.date(2025, 11, 15),
            event_end_date=datetime.date(2025, 11, 20),
            description="Mid-term examinations for all grades.",
            category="Exams",
            type="Putri"
        )
        self.valid_payload = {
            'event_name': 'Parent-Teacher Meeting',
            'event_start_date': '2025-10-10',
            'event_end_date': '2025-10-10',
            'description': 'Meeting with parents.',
            'category': 'Meeting',
            'type': 'Putra'
        }
        self.invalid_payload = {
            'event_name': '', # Event name is required
            'event_start_date': '2025-12-01',
            'event_end_date': '2025-12-05',
            'description': 'Winter break.',
            'category': 'Holiday',
            'type': 'Putri'
        }

    def test_get_all_events(self):
        """
        Ensure we can retrieve all academic calendar events.
        """
        url = reverse('academiccalendar-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_event(self):
        """
        Ensure we can retrieve a single event.
        """
        url = reverse('academiccalendar-detail', kwargs={'pk': self.event1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = AcademicCalendarSerializer(self.event1)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_event(self):
        """
        Ensure we can create a new academic calendar event with valid data.
        """
        url = reverse('academiccalendar-list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AcademicCalendar.objects.count(), 3)

    def test_create_invalid_event(self):
        """
        Ensure we cannot create a new academic calendar event with invalid data.
        """
        url = reverse('academiccalendar-list')
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_event(self):
        """
        Ensure we can update an existing event.
        """
        url = reverse('academiccalendar-detail', kwargs={'pk': self.event1.pk})
        updated_data = self.valid_payload
        updated_data['event_name'] = "Updated Event Name"
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event1.refresh_from_db()
        self.assertEqual(self.event1.event_name, "Updated Event Name")

    def test_delete_event(self):
        """
        Ensure we can delete an event.
        """
        url = reverse('academiccalendar-detail', kwargs={'pk': self.event1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AcademicCalendar.objects.count(), 1)
