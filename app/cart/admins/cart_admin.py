from django.contrib import admin
from cart.models.cart_model import CartModel


@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):

    """ Admin for Cart Model. """
    
    list_display = (
        "uuid",
        "user",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user__username",
    )
    search_fields = (
        "uuid",
        "user__first_name",
        "user__last_name",
        "user__username",
    )
    ordering = ("user", )
    date_hierarchy = "created_at"

    fields = ("user", )
    readonly_fields = ("user", )
