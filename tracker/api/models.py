from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Child(models.Model):
    """
    Model for storing a child's info of a user

    Basically a parent user will signup, and add a child/children,
    with one to many relation. 
    
    Children are not allowed to signup/login
    """
    class Meta:
        verbose_name_plural = "children"

    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ChildLocation(models.Model):
    """
    Model for storing user location at given timestamp
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    # NOTE
    # quick geography tips !!!
    # 3 digits will be need for lat/lng and 6 for decimal places
    # max lat 90 and max lng 180
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'ChildLocation: (' + str(Decimal(self.lat)) + ', ' + str(Decimal(self.lng)) + ')'


