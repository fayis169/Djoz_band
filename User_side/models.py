from django.db import models

# Create your models here.

class regDB(models.Model):
    band_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    loc = models.CharField(max_length=200, null=True, blank=True)
    cat = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="Image", null=True, blank=True)
    audio = models.FileField(upload_to="music", null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=300, null=True, blank=True)

class bookDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    b_name = models.CharField(max_length=100, null=True, blank=True)
    b_mobile = models.IntegerField(null=True, blank=True)
    b_email = models.EmailField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    loc = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)

class u_sign(models.Model):
    name = models.CharField(max_length=100)
    u_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    pas = models.CharField(max_length=50)
    mobile = models.IntegerField()

class u_contactDB(models.Model):
    c_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    web = models.CharField(max_length=200, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

class feedbackDB(models.Model):
    b_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    feedback = models.CharField(max_length=500, null=True, blank=True)

