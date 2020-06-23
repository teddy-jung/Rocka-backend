from django.db import models

from member.models import Member, Coupon
from product.models import Product, Color

class Order(models.Model):
    order_number            = models.IntegerField(default=0)
    payment_method          = models.ForeignKey('PaymentMethod', on_delete=models.SET_NULL, null=True)
    order_status            = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)
    shipping_address        = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, null=True)
    shipping_information    = models.ForeignKey('ShippingInformation', on_delete=models.SET_NULL, null=True)
    member                  = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    total_price             = models.DecimalField(max_digits=10, decimal_places=2)
    message                 = models.ForeignKey('Message', on_delete=models.SET_NULL, null=True)
    coupon                  = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True)
    use_coupon              = models.BooleanField(default=0)
    product                 = models.ManyToManyField(Product, through='Cart')

    class Meta:
        db_table = 'orders'


class OrderStatus(models.Model):
    name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'orderstatus'

class PaymentMethod(models.Model):
    name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'payment_methods'

class ShippingAddress(models.Model):
    destination     = models.CharField(max_length=100)
    recipient       = models.CharField(max_length=50)
    address         = models.CharField(max_length=2000)
    phone_number    = models.CharField(max_length=50)
    member          = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    is_default      = models.BooleanField(default=True)

    class Meta:
        db_table = 'shipping_addresses'

class ShippingInformation(models.Model):
    shipping_date_info      = models.CharField(max_length=100)
    shipping_charge         = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'shipping_information'

class Message(models.Model):
    name    = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'messages'

class Cart(models.Model):
    quantity    = models.CharField(max_length=50)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    order       = models.ForeignKey(Order, on_delete=models.CASCADE)
    color       = models.ForeignKey(Color, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'
