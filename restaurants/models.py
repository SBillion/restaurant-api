from django.db import models

class Restaurant(models.Model):
    """Restaurant Model
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    def __repr__(self):
        return self.name
