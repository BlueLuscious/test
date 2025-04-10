from decimal import Decimal
from django.db import models
from cart.models.cart_model import CartModel


class CartItemModel(models.Model):

    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name="items")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    metadata = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item de Carrito"
        verbose_name_plural = "Items de Carrito"
    
    def __str__(self) -> str:
        return f"Cart Item {self.id}"
    
    @property
    def total_price(self) -> Decimal:
        return self.price * self.quantity
    