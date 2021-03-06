from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=0.0
    )
    large_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=0.0
    )
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=0.0
    )

    # A menu item must have at least a price
    def clean(self):
        super().clean()

        if not self.small_price and not self.large_price and not self.price:
            raise ValidationError(_("A menu Item must have at least one price"))

    def __str__(self):
        return self.name


class Extra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=0.0
    )

    def __str__(self):
        return self.name


class OrderedItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    extras = models.ManyToManyField(Extra, blank=True, related_name="extras")

    def __str__(self):
        return f"{self.item} with {(list(self.extras) or '')}"


# The table will contain info about all orders made by users
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, related_name="ordered_items")

    def __str__(self):
        return f"Order made by: {self.user} and contains {list(self.items)}"
