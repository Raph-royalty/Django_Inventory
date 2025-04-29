from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name="home"),
    path('/create', views.create_view, name="product_create"),
    path('/list', views.product_view, name="product_list"),
    path('/update/<int:product_id>/', views.product_update, name="product_update"),
    path('/delete/<int:product_id>/', views.product_delete, name="product_delete"),
]
