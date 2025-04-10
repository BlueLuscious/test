from django.contrib import admin
from cart.models.cart_item_model import CartItemModel


@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):

    """ Admin for Cart Item Model. """
    
    list_display = (
        "id",
        "cart",
        "price",
        "stock",
        "quantity",
    )
    search_fields = (
        "id",
        "cart__uuid",
        "cart__user__first_name",
        "cart__user__last_name",
        "cart__user__username",
    )
    ordering = ("-created_at", )
    