from django.urls import path
from ShopApp.views import *
urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('forget/', forget),
    path('register_store/', register_store),
    path('add_goods/', add_goods),
    path('goods_list/', goods_lists),
]
