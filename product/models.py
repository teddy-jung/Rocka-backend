from django.db import models
#from order.models import ShippingInformation

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name                    = models.CharField(max_length=50)
    simple_description      = models.CharField(max_length=100)
    price                   = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_information    = models.ForeignKey('order.ShippingInformation', on_delete=models.SET_NULL, null=True)
    basic_information       = models.ForeignKey('BasicInformation', on_delete=models.SET_NULL, null=True)
    weight                  = models.DecimalField(max_digits=10, decimal_places=2)
    usage                   = models.CharField(max_length=50)
    kfda_audit              = models.CharField(max_length=100)
    caution                 = models.CharField(max_length=1000)
    color                   = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    is_soldout              = models.BooleanField(default=0)
    manufacturer            = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)
    outer_back_image_url    = models.URLField(max_length=2000, null=True)
    outer_front_image_url   = models.URLField(max_length=2000, null=True)
    inner_image_url         = models.URLField(max_length=2000, null=True)
    category                = models.ManyToManyField(Category, through='CategoryProduct')

    class Meta:
        db_table = 'products'

class CategoryProduct(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories_products'

class Color(models.Model):
    name            = models.CharField(max_length=50)
    color_url       = models.URLField(max_length=2000, null=True)
    ingredient_info = models.CharField(max_length=2000, null=True)
    stock_quantity  = models.IntegerField(default=1000)

    class Meta:
        db_table = 'colors'

class BasicInformation(models.Model):
    main_spec           = models.CharField(max_length=50)
    counseling_info     = models.CharField(max_length=500)
    return_policy       = models.CharField(max_length=2000)
    expiration_date     = models.CharField(max_length=50)
    country             = models.CharField(max_length=50)
    quality_assurance   = models.CharField(max_length=200)
    vendor              = models.CharField(max_length=50)

    class Meta:
        db_table = 'basicinformation'

class Manufacturer(models.Model):
    name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'manufacturers'
