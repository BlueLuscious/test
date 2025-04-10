from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import uuid4
from django.db import models
from client.models.client_model import ClientModel
if TYPE_CHECKING:
    from django.db.models import QuerySet
    from cart.models.cart_item_model import CartItemModel


class CartModel(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user = models.OneToOneField(ClientModel, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    items: "QuerySet[CartItemModel]"

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self) -> str:
        return f"Cart {self.uuid} - {self.user.username}"
    
    @property
    def total_amount(self) -> Decimal:
        return sum(item.total_price for item in self.items.all())
    