from django.db import models

class Store(models.Model):
    sortation       = models.CharField(max_length=50)
    branch_name     = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=50)
    store_address   = models.CharField(max_length=200)
    operating_time  = models.CharField(max_length=100)
    location_url    = models.URLField(max_length=2000)

    class Meta:
        db_table = 'stores'
