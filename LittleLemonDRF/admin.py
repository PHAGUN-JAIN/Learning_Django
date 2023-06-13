from django.contrib import admin
from .models import Book, Rating

# Register your models here.
admin.site.register(
    Book,
)  # the model is registered here so that we can use it from the admin panel
