
import json
from django.http import HttpResponse
# Create your views here.
def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')


def facts(request):
    response = request.get("https://catfact.ninja/fact")
    data = json.loads(response.content)
    return HttpResponse(data["fact"])


