from django.urls import path
from . import views
from .views import return_policy
app_name='listings'
urlpatterns = [
    path("",views.product_list,name='product_list'),
    path("search/",views.search,name='search'),
    path("trending/",views.trending,name='trending'),
    path("discounted/",views.discounted,name='discounted'),
    path("gift/",views.gift,name='gift'),
    path("*aw*/",return_policy.as_view(),name='gift'),
    path('<slug:category_slug>',views.product_list,name='product_list_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.product_detail,name='product_detail'),
]
