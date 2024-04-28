from django.urls import path
from . import views

app_name = "BE_table"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('insert', views.insert, name='insert'),
    path('report', views.report, name='report'),
    path('edit/<int:record_id>', views.edit, name='edit'),
    path('export_to_excel', views.export_to_excel, name='export_to_excel'),

]