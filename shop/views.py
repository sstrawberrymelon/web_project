
import json
from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Item


# Create your views here.
def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')


def facts(request):
    response = request.get("https://catfact.ninja/fact")
    data = json.loads(response.content)
    return HttpResponse(data["fact"])

def list_items(request):
    queryset = Item.objects.all() #получили весь список
    return render(request, 'list_item.html', context={'all_items': queryset})


def detail_items(request, pk, *args, **kwargs):
    item = Item.objects.get(pk=pk)
    return render(request, template_name='detail_itam.html', context={'item':item})

