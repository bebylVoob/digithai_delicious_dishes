from django.urls import path

from .views import cuisine_views

app_name = 'cuisine'

urlpatterns = [
    path('', cuisine_views)
]
