from django.contrib import admin
from .models import Pizza, Toppings, Subs, Salads, Pasta, DinnerPlatter

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatter)
