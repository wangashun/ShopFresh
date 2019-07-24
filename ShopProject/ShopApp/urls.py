from django.urls import path, re_path
from ShopApp.views import *
urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('forget/', forget),
    path('register_store/', register_store),
    path('add_goods/', add_goods),
    path('goods_list/', goods_lists),
    re_path('^all_goods/(?P<goods_id>\d+)', all_goods),
    re_path('update_goods/(?P<goods_id>\d+)', update_goods),
]
