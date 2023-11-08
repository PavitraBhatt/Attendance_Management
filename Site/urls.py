from . import views
from django.urls import path
from .views import SiteGetView,SiteGetIdView,SiteUpdateView,SitePostView,SiteDeleteView,SiteDetailView,SiteCreateView

urlpatterns = [
    path('site/',views.site_list),
    path('api/site/detail/<int:pk>/', SiteDetailView.as_view(), name='site_detail'),
    path('api/site/create/', SiteCreateView.as_view(), name='site_create'),
    path('site_get/', SiteGetView.as_view(), name='site-get'),
    path('api/site/<str:SiteID>/', SiteGetIdView.as_view(), name='site_get_id'),
    path('api/site_update/<str:SiteID>/', SiteUpdateView.as_view(), name='site_update'),
    path('api/site/post/', SitePostView.as_view(), name='site_post'),
    path('api/site/delete/', SiteDeleteView.as_view(), name='site_delete'),
]
