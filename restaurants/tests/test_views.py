from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json

from ..models import Restaurant
from ..serializers import RestaurantSerializer


class GetRestaurantListTest(APITestCase):
    """Test the view to get all restaurants"""

    def setUp(self) -> None:
        Restaurant.objects.create(name="Funky burger")
        Restaurant.objects.create(name="Toto Pizza")
        Restaurant.objects.create(name="Le snack du pont")
        Restaurant.objects.create(name="Le balcon")
        Restaurant.objects.create(name="L'amie rabelle")
        Restaurant.objects.create(name="Flocon de sel ")
        Restaurant.objects.create(name="Les cèdres")
        Restaurant.objects.create(name="Les tontons")

    def test_get_all_restaurants(self) -> None:
        response = self.client.get(reverse("restaurants"))
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetRestaurantDetailTest(APITestCase):
    def setUp(self) -> None:
        self.funky_burger = Restaurant.objects.create(name="Funky burger")
        self.toto_pizza = Restaurant.objects.create(name="Toto Pizza")
        self.tontons = Restaurant.objects.create(name="Les tontons")

    def test_get_valid_restaurant(self) -> None:
        response = self.client.get(
            reverse("restaurant_detail", kwargs={"pk": self.funky_burger.pk})
        )
        serializer = RestaurantSerializer(self.funky_burger)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_restaurant(self) -> None:
        response = self.client.get(
            reverse("restaurant_detail", kwargs={"pk": 600})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateRestaurantTest(APITestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'name': 'Super restaurant',
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_create_valid_restaurant(self):
        response = self.client.post(
            reverse('restaurants'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_restaurant(self):
        response = self.client.post(
            reverse('restaurants'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)