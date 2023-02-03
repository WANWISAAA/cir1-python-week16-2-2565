from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/',include('member/urls.py'))
    #path('index/',include('member.urls'))
]