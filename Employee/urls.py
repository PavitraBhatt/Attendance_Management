from . import views
from django.urls import path
from .views import EmployeeCreateView
from .views import EmployeeGetView
from .views import EmployeeGetIdView
from .views import EmployeePostView
from .views import EmployeeUpdateView
from .views import EmployeePutView
from .views import EmployeeDeleteView


urlpatterns = [
    # Other URL patterns
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/get/', EmployeeGetView.as_view(), name='employee-get'),
    path('employee/get/<str:EmployeeID>/', EmployeeGetIdView.as_view(), name='employee-get-id'),
    path('employee/post/', EmployeePostView.as_view(), name='employee-post'),
    path('employee/update/<str:EmployeeID>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/put/', EmployeePutView.as_view(), name='employee-put'),
    path('employee/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

]