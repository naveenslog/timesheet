from django.db import models
from django.conf import settings

class Abstract(models.Model):
    """
    Abstract Model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(Abstract):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Attendance(Abstract):
    employee = models.ForeignKey(settings.EMPLOYEE_MODEL, on_delete=models.CASCADE, blank=True)
    date = models.DateField(blank=True, null=True, default=None)
    in_time = models.TimeField(blank=True, null=True, default=None)
    out_time = models.TimeField(blank=True, null=True, default=None)
    overtime_hours = models.IntegerField(blank=True, null=True, default=None)

    @property
    def get_hours(self):
        return self.out_time - self.in_time

    class Meta:
        unique_together = ("employee", "date")