from django.db import models
from account.models import Account


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return f"{self.title}"




def get_product_image_filepath(self, filename):
    return 'product/product_images/None/product_image.png'


def get_default_product_image():
    return 'product/product_default_images/default_product_image.png'


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_product_image_filepath, default=get_default_product_image, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    



class Order(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField(blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"




class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.product.title}"



class Cart(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.title}"