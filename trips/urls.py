from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_trip, name='create_trip'),
    path('trip/<str:trip_code>/', views.trip_detail, name='trip_detail'),
    path('trip/<str:trip_code>/preferences/', views.submit_preference, name='submit_preference'),
]
