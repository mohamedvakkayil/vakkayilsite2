from django.urls import path
from .import views

app_name = 'hom'
urlpatterns=[
    path('',views.index, name='index')
] 