from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MurojaatViewSet

router = DefaultRouter()
router.register(r'letters', MurojaatViewSet, basename='murojaat')

urlpatterns = [
    path('submit/', views.submit_murojaat, name='submit_murojaat'),
    path('status/', views.murojaat_status, name='murojaat_status'),
    path('analytics/', views.analytics, name='analytics'),
    path('api/', include(router.urls)),
]

