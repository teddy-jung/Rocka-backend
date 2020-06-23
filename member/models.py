from django.db import models

class Member(models.Model):
    username        = models.CharField(max_length=50)
    password        = models.CharField(max_length=50)
    realname        = models.CharField(max_length=50)
    email           = models.CharField(max_length=200)
    phone_number    = models.CharField(max_length=50)
    address         = models.CharField(max_length=2000, null=True)
    gender          = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    coupon          = models.ManyToManyField('Coupon', through='MemberCoupon')

    class Meta:
        db_table = 'members'

class Gender(models.Model):
    name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'genders'

class Coupon(models.Model):
    name            = models.CharField(max_length=50)
    benefit         = models.CharField(max_length=50)
    coupon_coverage = models.CharField(max_length=50)
    possible_period = models.CharField(max_length=100)

    class Meta:
        db_table = 'coupons'

class MemberCoupon(models.Model):
    member  = models.ForeignKey(Member, on_delete = models.CASCADE)
    coupon  = models.ForeignKey(Coupon, on_delete = models.CASCADE)

    class Meta:
        db_table = 'members_coupons'

class Inquiry(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    member      = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    by_email    = models.BooleanField(default=1)

    class Meta:
        db_table = 'inquiries'

class AttachedFile(models.Model):
    name    = models.CharField(max_length=1000)
    inquiry = models.ForeignKey(Inquiry, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'attached_files'

