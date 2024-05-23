from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MurojaatViewSet

router = DefaultRouter()
router.register(r'letters', MurojaatViewSet, basename='murojaat')

urlpatterns = [
    path('', views.murojaat_index, name='index'),
    path('about/', views.murojaat_about, name='murojaat_about'),
    path('contact/', views.murojaat_contact, name='murojaat_contact'),
    path('statistika/', views.murojaat_statistika, name='murojaat_statistika'),

    # path('submit/', views.submit_murojaat, name='submit_murojaat'),
    # path('status/', views.murojaat_status, name='murojaat_status'),
    # path('analytics/', views.analytics, name='analytics'),
    path('api/', include(router.urls)),
]

