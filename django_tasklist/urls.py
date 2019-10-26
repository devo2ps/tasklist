from django.contrib import admin
from django.urls import path
from mc_tasklist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add),
    path('remove', views.remove),
    path('', views.index),
]
