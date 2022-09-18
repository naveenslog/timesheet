from django_filters.filters import (
    CharFilter,
    NumberFilter,
    DateFilter,
)
from django_filters import FilterSet
from timesheet.models import Attendance

class TimesheetFilter(FilterSet):
    print("Called")
    start = CharFilter(method="filter_start")
    end = CharFilter(method="filter_end")
    year = DateFilter(field_name="date", lookup_expr="year")
    month = DateFilter(field_name="date", lookup_expr="month")
    employee = NumberFilter(field_name="employee__id", lookup_expr="exact")

    def filter_start(self, queryset, name, value):
        return queryset.filter(date__gte=value)

    def filter_end(self, queryset, name, value):
        return queryset.filter(date__lte=value)

    class Meta:
        model = Attendance
        fields = [
            "start",
            "end",
            "year",
            "month",
            "employee"
        ]
