from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Pizza(models.Model):
    dish = models.CharField(max_length=60)
    pizza_type = models.CharField(
        max_length=10, choices=[('Regular', 'Regular'), ('Sicilian', 'Sicilian')])
    price_small = models.FloatField()
    price_large = models.FloatField()
    Toppings = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.dish} {self.pizza_type} "


class Toppings(models.Model):
    topping = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.topping}"

class Subs(models.Model):
    sub_name = models.CharField(max_length=60)
    price_small = models.FloatField()
    price_large = models.FloatField()

    def __str__(self):
        return f"{self.sub_name}"


class Pasta(models.Model):
    pasta_name = models.CharField(max_length=60)
    price = models.FloatField()

    def __str__(self):
        return f"{self.pasta_name} "


class Salads(models.Model):
    salad_name = models.CharField(max_length=60)
    price = models.FloatField()

    def __str__(self):
        return f"{self.salad_name} "


class DinnerPlatter(models.Model):
    plate_name = models.CharField(max_length=60)
    price_small = models.FloatField()
    price_large = models.FloatField()

    def __str__(self):
        return f"{self.plate_name} "
