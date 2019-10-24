from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restaurants import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='restaurants'),
    path('<int:pk>/', views.RestaurantDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)