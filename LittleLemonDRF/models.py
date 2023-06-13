from django.db import models


# Create your models here.
class Rating(models.Model):
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = (models.Index(fields=["price"]),)
