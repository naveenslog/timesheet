from django.urls import path, include
from rest_framework.routers import DefaultRouter
from timesheet import views

router = DefaultRouter()
router.register("in-out", views.InOutViewSet, basename="timesheet")
router.register("", views.AttendanceViewSet, basename="timesheet")

urlpatterns = router.urls
