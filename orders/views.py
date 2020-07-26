from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza, Pasta, Subs, Salads, Toppings, DinnerPlatter

# Create your views here.
def home(request):
    context = {
        'pizzas' : Pizza.objects.all(),
        'pastas' : Pasta.objects.all(),
        'subs' : Subs.objects.all(),
        'salads' : Salads.objects.all(),
        'toppings' : Toppings.objects.all(),
        'dinnerplatters' : DinnerPlatter.objects.all()
    }
    return render(request, "orders/index.html", context)
