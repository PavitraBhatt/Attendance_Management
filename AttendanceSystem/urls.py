from django.urls import path
from AttendanceSystem.views import AttendenceCreateView, AttendanceUpdateView,AttendanceGetIdView,AttendanceDeleteView

urlpatterns = [
    path('api/attendance/create/',AttendenceCreateView.as_view(), name = 'attendance_create'),
    path('api/attendance_update/<int:id>/',AttendanceUpdateView.as_view(), name = 'attendance_update'),
    path('api/attendance/<int:id>/',AttendanceGetIdView.as_view(), name = 'attendance_get_id'),
    path('api/attendance/delete/', AttendanceDeleteView.as_view(), name='attendance_delete'),
]


