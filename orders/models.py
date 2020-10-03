from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False, null=False, default=0.0
    )

    class Meta:
        abstract = True


class MenuItem(Item):
    def clean(self):
        super().clean()

        if not self.price:
            raise ValidationError(_("A menu Item must have at least one price"))

    def __str__(self):
        return self.name


# The table will contain info about all orders made by users
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    total = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)

    @property
    def _total_from_items(self):
        _total = 0
        for item in self.items:
            _total = _total + item.total
        return _total

    def clean(self):
        super().clean()

        if self._total_from_items != self.total:
            raise ValidationError(_("Error: total price of items isn't consistent"))

        if not self.items:
            raise ValidationError(_("A shopping cart must have at least one item"))

    def __str__(self):
        return f"Order made by: {self.user} and contains {self.items}"


class CartItem(Item):
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    @property
    def total(self):
        return float(self.price) * self.quantity

    def clean(self):
        super().clean()

        if not self.quantity:
            raise ValidationError(_("A Cart Item must have at least a quantity of one"))

    def __str__(self):
        return super().__str__()
