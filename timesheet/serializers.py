from datetime import datetime
from rest_framework import serializers
from timesheet.models import Attendance
from account.serializers import CustomUserSerializer
from datetime import datetime


class AttendanceSerializer(serializers.ModelSerializer):

    employee = CustomUserSerializer(read_only=True, required=False)

    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, data):
        if data.get("date") is not None and data.get("date") > datetime.now().date():
            raise serializers.ValidationError("Future dates are not allowed")
        else:
            return data

    def create(self, validated_data):
        request = self.context["request"]
        attendance = Attendance.objects.filter(
            employee=request.user,
            date=validated_data.get("date")
        ).first()
        if attendance is not None:
            return attendance
        else:
            validated_data.update({"employee": request.user})
            return super().create(validated_data)