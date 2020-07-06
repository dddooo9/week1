from django.urls import path
from . import views

app_name="choice"
urlpatterns = [
    path('door1/', views.door1, name="door1"),
    path('door2/', views.door2, name="door2"),
    path('door3/', views.door3, name="door3"),
    path('door11/', views.door11, name="door11"),
    path('door13/', views.door13, name="door13"),
    path('door22/', views.door22, name="door22"),
    path('door23/', views.door23, name="door23"),
    path('door32/', views.door32, name="door32"),
    path('door33/', views.door33, name="door33"),
]