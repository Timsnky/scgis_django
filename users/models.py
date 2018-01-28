# Imports
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

#   Models
#
#The membership levels model
class MembershipLevel(models.Model):
    name = models.CharField(max_length=45)
    amount = models.IntegerField(default = 0)
    expires = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def getAmount(self):
        return self.amount

#Payment methods model
class PaymentMethod(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

#Title methods model
class Title(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#Country model
class Country(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

#Theme model
class Theme(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

#UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
    organization = models.CharField(max_length = 254, blank=True)
    job_title = models.CharField(max_length = 254, blank=True)
    phone = models.CharField(max_length = 45, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/members/', blank=True)
    city = models.CharField(max_length = 45, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length = 255, blank=True)
    state = models.CharField(max_length = 45, blank=True)
    zip = models.CharField(max_length = 45, blank = True)
    latitude = models.DecimalField(max_digits=25, decimal_places = 15, null=True, blank = True)
    longitude = models.DecimalField(max_digits=25, decimal_places = 15, null=True, blank = True)
    chapter = models.IntegerField(default=4)
    subscribejobs = models.IntegerField(default = 0)
    membership_level = models.ForeignKey(MembershipLevel, on_delete=models.SET_NULL, null=True)
    membership_expiry = models.DateField(null = True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    login_attempts = models.IntegerField(default=0)
    last_login = models.DateTimeField(auto_now = True)
    activation = models.TextField(max_length = 255, blank = True)
    pwdresetkey = models.TextField(max_length = 255, blank = True)
    remember_token = models.TextField(max_length = 255, blank = True)
    listserv = models.IntegerField(default=0)
    featured = models.IntegerField(default=0)
    accept_internal_messages = models.IntegerField(default=1)
    notify_internal_messages = models.IntegerField(default=1)
    public = models.IntegerField(default=1)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def getUser(self):
        return self.user
