from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def discounted_price(self):
        return self.price * (1 - self.discount / 100)
    
    def total_price(self):
        return self.discounted_price() * self.quantity

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)