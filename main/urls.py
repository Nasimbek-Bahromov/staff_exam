from django.urls import path, include
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.dashboard, name = 'index'),
    path('api/', include('api.urls')),
]
