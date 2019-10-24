from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Restaurant
from ..serializers import RestaurantSerializer


class GetAllRestaurantsTest(APITestCase):
    """Test the view to get all restaurants"""

    def setUp(self) -> None:
        Restaurant.objects.create(name='Funky burger')
        Restaurant.objects.create(name='Toto Pizza')
        Restaurant.objects.create(name='Le snack du pont')
        Restaurant.objects.create(name='Le balcon')
        Restaurant.objects.create(name='L\'amie rabelle' )
        Restaurant.objects.create(name='Flocon de sel ')
        Restaurant.objects.create(name='Les cèdres')
        Restaurant.objects.create(name='Les tontons')

    def test_get_all_restaurants(self):
        response = self.client.get(reverse('restaurants'))
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

