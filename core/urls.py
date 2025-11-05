from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('htmx-demo/', views.htmx_demo, name='htmx_demo'),
]
