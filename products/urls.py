from django.urls import path
from . import views


urlpatterns = [
    path('publish/', views.publish, name = "上傳動物頁面"),
    
]
