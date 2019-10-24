from django.urls import path

from restaurants import views

urlpatterns = [
    path("", views.RestaurantList.as_view(), name="restaurants"),
    path("<int:pk>/", views.RestaurantDetail.as_view(), name="restaurant_detail"),
]
