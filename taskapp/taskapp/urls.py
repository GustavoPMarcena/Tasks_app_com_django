from django.contrib import admin
from django.urls import path, include
from tap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tap.urls"))
]
