from django.urls import path
from .views import view_product


app_name = "product"
urlpatterns = [
    path("", view_product, name="products"),
]
