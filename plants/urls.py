from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('upload_excel', views.upload_excel, name='upload_excel'),
    url('casting_plan', views.casting_plan, name='casting_plan'),

]
