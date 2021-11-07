from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    # path('hello/', views.myview),
    path('hello/', views.myview),
    ]