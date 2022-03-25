
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # keyword = value
    query_set = Product.objects.filter(last_update__year = 2021)

    return render(request, 'hello.html', {'name': 'Sayem', 'products': list(query_set)})
