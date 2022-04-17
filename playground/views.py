
from django.shortcuts import render
from store.models import Order, Product

def say_hello(request):
    query_set =  Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'Sayem', 'result': list(query_set)})
