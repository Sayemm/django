
from django.shortcuts import render
from store.models import Collection, Product

def say_hello(request):
    query_set = Product.objects.filter(pk = 0).first()

    print(query_set)

    return render(request, 'hello.html', {'name': 'Sayem'})