from django.db import models


class Temp(models.Model):
    title = models.CharField('Title', max_length=50)
    designe = models.ImageField(null=True, blank=True, upload_to='images/')
    link = models.CharField('link', max_length=100)
    phone = models.CharField('mobile', max_length=50)
    mail = models.EmailField('email')
    price = models.CharField('price', max_length=50, blank=True)
