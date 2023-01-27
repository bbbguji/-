from django.db import models

class ProductModel(models.Model):
    pname =  models.CharField(max_length=100, blank=True, default='', null=False)
    pprice = models.IntegerField(default=0, blank=True ,null=False)
    pimages = models.CharField(max_length=100, blank=True, default='')
    pdescription = models.TextField(blank=True, default='')
    def __str__(self):
        return self.pname
        
class OrdersModel(models.Model):
    subtotal = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    grandtotal = models.IntegerField(default=0)
    customname =  models.CharField(max_length=100, default='')
    customemail =  models.CharField(max_length=100, default='')
    customaddress =  models.CharField(max_length=100, default='')
    customphone =  models.CharField(max_length=100, default='')
    paytype =  models.CharField(max_length=50, default='')
    def __str__(self):
        return self.customname
     
class DetailModel(models.Model):
    dorder = models.ForeignKey('OrdersModel', on_delete=models.CASCADE)
    pname = models.CharField(max_length=100, default='')
    unitprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    dtotal = models.IntegerField(default=0)
    def __str__(self):
        return self.pname
class AlbumModel(models.Model):
    adate = models.DateTimeField(auto_now=True)
    alocation = models.CharField(max_length=200, blank=True, default='')
    atitle = models.CharField(max_length=100, null=False)
    adesc = models.TextField(blank=True, default='')
    def __str__(self):
        return self.atitle

class PhotoModel(models.Model):
    palbum = models.ForeignKey('AlbumModel', on_delete=models.CASCADE)
    psubject = models.CharField(max_length=100, null=False)
    pdate = models.DateTimeField(auto_now=True)
    purl = models.CharField(max_length=100, null=False)
    phit = models.IntegerField(default=0)
    def __str__(self):
        return self.psubject
