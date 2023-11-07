from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HRDetailView
from .views import HRListView
from .views import HRCreateView
from .views import HRGetView
from .views import HRPostView
from .views import HRPutView
from .views import HRUpdateView
from .views import HRDeleteView




urlpatterns = [
    path('hr_detail/<str:pk>/', HRDetailView.as_view(), name='hr_detail'),
    path('hr_list/', HRListView.as_view(), name='hr_list'),
    path('hr_create/', HRCreateView.as_view(), name='hr_create'),
    path('hr_get/', HRGetView.as_view(), name='hr_get'),
    path('hr_get/<str:HRID>/', HRGetView.as_view(), name='hr_get_with_id'),
    path('hr_post/', HRPostView.as_view(), name='hr_post'),
    path('hr_put/', HRPutView.as_view(), name='hr_put'),
    path('hr_update/<str:HRID>/', HRUpdateView.as_view(), name='hr_update'),
    path('hr_delete/', HRDeleteView.as_view(), name='hr_delete'),
]
