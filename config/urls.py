from django.contrib import admin
from django.urls import path
from vazifa import views  # views.py qaerda bo‘lsa shuni yoz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('', views.contact, name='contact'),
    path('', views.our, name='our'),
]