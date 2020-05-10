from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('login', views.login, name='login'),
    url('logout', views.user_logout, name='logout'),
    url('index', views.index, name='index'),
    url('dashboard', views.dashboard, name='dashboard'),
    url('list_user', views.list_user, name='list_user'),
    url('add_user', views.add_user, name='add_user'),
    url('view_user', views.view_user, name='view_user'),
    url('edit_user', views.edit_user, name='edit_user'),
    url('del_user', views.del_user, name='del_user'),
    url('bulk_import', views.bulk_import, name='bulk_import'),
    url('bulk_template', views.bulk_template, name='bulk_template'),
    url('export_users_as_csv', views.export_users_as_csv, name='export_users_as_csv'),
    url('list_roles', views.list_roles, name='list_roles'),
    url('role', views.role, name='role'),
    url('stat', views.statics, name='stat'),
]
