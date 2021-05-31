
from django.urls import path
from django.urls.conf import include
from .views import add_product_view, ProductListView, ProductDelete

app_name = "products"

urlpatterns = [
    path('add/',add_product_view,name='add_product'),
    path('list/',ProductListView.as_view(),name='list_product'),
    path('delete/<int:pk>/',ProductDelete.as_view(), name="delete_view"),
]
