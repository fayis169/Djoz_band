from django.db import models

# Create your models here.
class asignup(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    u_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    pas = models.CharField(max_length=50, null=True, blank=True)
    mob = models.IntegerField(null=True, blank=True)