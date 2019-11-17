#交由這邊來負責
#這邊是account的view ，專門處理account的註冊和登入 依照網址來決定啟用的功能(view)

from django.urls import path
from . import views #記得從本目錄('.')import views 近來 才可以使用本目錄的view 也就是account.views.py


urlpatterns = [
    path('signup/', views.signup ,name='註冊頁面'),  #如果網址為signup/ 將會啟動本目錄的views.signup  且命名為"註冊頁面""
]
