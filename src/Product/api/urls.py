from django.db import router
from django.urls import path, include
from rest_framework import urlpatterns
from Product.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud',views.ProductViewSet,basename='product')

urlpatterns = [
    path('',include(router.urls))
]