from django.urls import path
from . import views


urlpatterns = [
    path('publish/', views.publish, name = "上傳動物頁面"),
    path('update/', views.update_Json_To_DB, name = "更新DB"),
]
