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
        Restaurant.objects.create(name="Les nouveaux sauvages")
        Restaurant.objects.create(name="La plume")
        Restaurant.objects.create(name="La mauvaise herbe")
        Restaurant.objects.create(name="Les tchoutchous")
        Restaurant.objects.create(name="La ratatouiulle")

    def test_get_all_restaurants_paginated(self) -> None:
        response = self.client.get(reverse("restaurant-list"))
        restaurants = Restaurant.objects.all()
        serializer_first_page = RestaurantSerializer(restaurants[:10], many=True)
        self.assertEqual(response.data.get("results"), serializer_first_page.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse("restaurant-list"), {"page": 2})
        serializer_seconde_page = RestaurantSerializer(restaurants[10:], many=True)
        self.assertEqual(response.data.get("results"), serializer_seconde_page.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse("restaurant-list"), {"page_size": 50})
        serializer_all = RestaurantSerializer(restaurants, many=True)
        self.assertEqual(response.data.get("results"), serializer_all.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetRestaurantDetailTest(APITestCase):
    def setUp(self) -> None:
        self.funky_burger = Restaurant.objects.create(name="Funky burger")
        self.toto_pizza = Restaurant.objects.create(name="Toto Pizza")
        self.tontons = Restaurant.objects.create(name="Les tontons")

    def test_get_valid(self) -> None:
        response = self.client.get(
            reverse("restaurant-detail", kwargs={"name": self.funky_burger.name})
        )
        serializer = RestaurantSerializer(self.funky_burger)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid(self) -> None:
        response = self.client.get(
            reverse("restaurant-detail", kwargs={"name": "Wrong name"})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateRestaurantTest(APITestCase):
    """ Test for restaurant POST view"""

    def setUp(self) -> None:
        self.valid_payload = {"name": "Super restaurant"}
        self.invalid_payload = {"name": "", "blurp": "blirp"}

    def test_create_valid(self) -> None:
        response = self.client.post(
            reverse("restaurant-list"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self) -> None:
        response = self.client.post(
            reverse("restaurant-list"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateRestaurantTest(APITestCase):
    """ Test for restaurant PUT view """

    def setUp(self) -> None:
        self.toto_pizza = Restaurant.objects.create(name="Toto Pizza")
        self.valid_payload = {"name": "Super restaurant"}
        self.invalid_payload = {"name": "", "blablabla": "plop"}

    def test_valid_update(self) -> None:
        response = self.client.put(
            reverse("restaurant-detail", kwargs={"name": self.toto_pizza.name}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.toto_pizza.refresh_from_db()
        serializer = RestaurantSerializer(self.toto_pizza)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_update(self) -> None:
        response = self.client.put(
            reverse("restaurant-detail", kwargs={"name": self.toto_pizza.name}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteRestaurantTest(APITestCase):
    """ Test for restaurant DELETE """

    def setUp(self):
        self.funky_burger = Restaurant.objects.create(name="Funky burger")
        self.toto_pizza = Restaurant.objects.create(name="Toto Pizza")
        self.tontons = Restaurant.objects.create(name="Les tontons")

    def test_valid_delete(self) -> None:
        response = self.client.delete(
            reverse("restaurant-detail", kwargs={"name": self.funky_burger.name})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self) -> None:
        response = self.client.delete(
            reverse("restaurant-detail", kwargs={"name": "Wrong name"})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetRestaurantRandomTest(APITestCase):
    """Test the view to get random restaurant"""

    def setUp(self) -> None:
        self.funky_burger = Restaurant.objects.create(name="Funky burger")
        self.toto_pizza = Restaurant.objects.create(name="Toto Pizza")
        self.tontons = Restaurant.objects.create(name="Les tontons")
        self.all_restaurant_serialized = RestaurantSerializer(
            Restaurant.objects.all(), many=True
        ).data

    def test_random(self) -> None:

        response = self.client.get(reverse("restaurant-random"))
        self.assertIn(response.data, self.all_restaurant_serialized)
        response = self.client.get(reverse("restaurant-random"))
        self.assertIn(response.data, self.all_restaurant_serialized)
