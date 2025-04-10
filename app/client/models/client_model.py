from typing import TYPE_CHECKING
from django.db import models
from django.contrib.auth.models import AbstractUser
if TYPE_CHECKING:
    from cart.models.cart_model import CartModel


class ClientModel(AbstractUser):

    cart: "CartModel"
    