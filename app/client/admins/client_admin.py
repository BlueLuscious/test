from django.contrib import admin
from client.models.client_model import ClientModel


@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    pass
