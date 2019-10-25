from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "name"

    @action(detail=False)
    def random(self, request) -> Response:
        return Response(self.get_serializer(Restaurant.get_random_faster()).data)
