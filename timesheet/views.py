from rest_framework import viewsets
from timesheet.models import Attendance
from timesheet.serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from timesheet.filters import TimesheetFilter
from django_filters.rest_framework import DjangoFilterBackend


class AttendanceViewSet(viewsets.ModelViewSet):
    """
    Attendance Viewset
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = TimesheetFilter

    def filter_queryset(self, queryset):
        filter_backends = (DjangoFilterBackend,)

        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)
        return TimesheetFilter(self.request.query_params, queryset).qs

class InOutViewSet(viewsets.ModelViewSet):
    """
    Inout Viewset
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAuthenticated,)
