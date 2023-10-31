from . import views
from django.urls import path

urlpatterns = [
    path('department/',views.department_list),
    path('department/<str:pk>',views.department_detail),
    path('departmentcreate/',views.department_create),
    path('getdepartment/',views.department_get),
    path('getdepartment/<str:DepartmentID>/',views.department_get_id),
    path('postdepartment/',views.department_post),
    path('updatesdepartment/<int:DepartmentID>/', views.department_update, name='department-update'),
    path('updatedepartment/',views.department_put),
    path('deletedepartment/',views.department_delete),
]
