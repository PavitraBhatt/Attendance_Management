from . import views
from django.urls import path

urlpatterns = [
    path('employee/',views.employee_list),
    path('employee/<str:pk>',views.employee_detail),
    path('employeecreate/',views.employee_create),
    path('getemployee/',views.employee_get),
    path('getemployee/<str:EmployeeID>/',views.employee_get_id),
    path('postemployee/',views.employee_post),
    path('updateemployee/<str:EmployeeID>/', views.employee_update, name='employee-update'),
    path('updateemployee/',views.employee_put),
    path('deleteemployee/',views.employee_delete),
]
