from . import views
from django.urls import path

urlpatterns = [
    path('site/',views.site_list),
    path('site/<str:pk>',views.site_detail),
    path('sitecreate/',views.site_create),
    path('getsite/',views.site_get),
    path('getsite/<str:SiteID>/',views.site_get_id),
    path('postsite/',views.site_post),
    # path('updatesite/',views.site_put),
    path('updatesite/<str:SiteID>/', views.site_update, name='site-update'),
    path('deletesite/',views.site_delete),
]
