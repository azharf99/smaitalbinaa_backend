from rest_framework import viewsets, permissions

from django.db import transaction
from teachers.models import Teacher
from .models import Tahfidz, Target, Tilawah
from .serializers import QuickTilawahCreateSerializer, TahfidzSerializer, TargetSerializer, TilawahSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.pagination import StandardResultsSetPagination
from utils.surat_quran import QURAN_SURAH

# Create your views here.

class TahfidzViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tahfidz records to be viewed or edited.
    """
    queryset = Tahfidz.objects.all().order_by('-created_at')
    serializer_class = TahfidzSerializer
    pagination_class = StandardResultsSetPagination


class TargetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tilawah Targets to be viewed or edited.
    """
    queryset = Target.objects.all().order_by('-tanggal')
    serializer_class = TargetSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """Optionally filters by `user_id` query parameter."""
        date = self.request.GET.get('date')
        if date:
            return super().get_queryset().filter(tanggal=date)
        
        return super().get_queryset()


class TilawahViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tilawah records to be viewed or edited.
    """
    queryset = Tilawah.objects.all().order_by('-tanggal', 'santri')
    serializer_class = TilawahSerializer
    pagination_class = StandardResultsSetPagination


class TilawahQuickCreateView(APIView):
   """
   API endpoint for bulk creating or updating Tilawah records.
   If a record for a given student and date already exists, it will be updated.
   Otherwise, a new record will be created.
   """
   permission_classes = [permissions.IsAuthenticated]

   def post(self, request, *args, **kwargs):
       serializer = QuickTilawahCreateSerializer(data=request.data)
       if serializer.is_valid():
            validated_data = serializer.validated_data
            created_count = 0
            updated_count = 0
            
            try:
                with transaction.atomic():
                    for student_data in validated_data['student_data']:
                        # Skip if essential data is missing for 'Hadir'
                        if student_data.get('kehadiran') == 'Hadir' and not (student_data.get('halaman') or student_data.get('surat')):
                            continue
                        
                        # Prepare the data for fields that will be updated or created.
                        defaults = {
                            'catatan': validated_data.get('catatan', ''),
                            'kehadiran': student_data.get('kehadiran'),
                            'halaman': student_data.get('halaman'),
                            'surat': student_data.get('surat'),
                            'ayat': student_data.get('ayat'),
                            'kelancaran': student_data.get('kelancaran'),
                            'tajwid': student_data.get('tajwid'),
                        }

                        # Use update_or_create to either update an existing record or create a new one.
                        tilawah_instance, created = Tilawah.objects.update_or_create(
                            tanggal=validated_data['tanggal'],
                            santri_id=student_data['santri_id'],
                            defaults=defaults
                        )
                        
                        # Set the many-to-many relationship now that the instance has an ID
                        tilawah_instance.pendamping.set(validated_data['pendamping_ids'])

                        if created:
                            created_count += 1
                        else:
                            updated_count += 1
            except Exception as e:
                return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'status': 'success', 'created_count': created_count, 'updated_count': updated_count}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurahListView(APIView):
    """
    A view to provide a list of all Quran surahs.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        surah_list = [{'id': surah[0], 'name': surah[1]} for surah in QURAN_SURAH]
        return Response(surah_list)