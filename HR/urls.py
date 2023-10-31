from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hr/',views.hr_list),
    path('hr/<str:pk>',views.hr_detail),
    path('hrcreate/',views.hr_create),
    path('gethr/<str:HRID>/',views.hr_get_id),
    path('gethr/',views.hr_get),
    path('posthr/',views.hr_post),
    path('updatehr/<str:HRID>/', views.hr_update, name='hr-update'),
    path('updatehr/',views.hr_put),
    path('deletehr/',views.hr_delete),
]