from django.contrib import admin
from django.urls import path,include
from Web_App import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('Web_App', include('Web_App.urls')),
]



