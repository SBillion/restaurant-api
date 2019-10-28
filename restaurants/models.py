import random

from django.db import models
from django.db.models import Max


class Restaurant(models.Model):
    """Restaurant Model
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    @classmethod
    def get_random(cls) -> object:
        """
        This method can be really slow on big table
        """
        return cls.objects.order_by("?").first()

    @classmethod
    def get_random_faster(cls) -> object:
        """
        This method to get a random object is faster but get slower if there is a lot of deletion.
        """
        max_id = cls.objects.all().aggregate(max_id=Max("id"))["max_id"]
        while True:
            pk = random.randint(1, max_id)
            restaurant = Restaurant.objects.filter(pk=pk).first()
            if restaurant:
                return restaurant

    def __repr__(self):
        return self.name
