from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)