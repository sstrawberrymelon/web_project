from django.urls import path
from shop.views import detail_items, list_items, greetings

from shop import views

urlpatterns = [
    path('shop/', views.list_items),
    path('shop/<int:pk>/', detail_items),
    path('', list_items),
    # path('facts/',cats),
    path('greeting/', greetings)
]
