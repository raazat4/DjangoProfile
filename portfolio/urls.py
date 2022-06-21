from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from portfolio import views
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 