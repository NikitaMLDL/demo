# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Partners(models.Model):
    partnerid = models.AutoField(primary_key=True)
    partnertype = models.CharField(max_length=50, blank=True, null=True)
    partnername = models.CharField(max_length=100, blank=True, null=True)
    directorname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    legaladdress = models.TextField(blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partners'


class Products(models.Model):
    productid = models.AutoField(primary_key=True)
    producttypeid = models.ForeignKey('Producttype', models.DO_NOTHING, db_column='producttypeid', blank=True, null=True)
    productname = models.CharField(max_length=255, blank=True, null=True)
    articul = models.CharField(max_length=10, blank=True, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Producttype(models.Model):
    producttypeid = models.AutoField(primary_key=True)
    producttype = models.CharField(max_length=255, blank=True, null=True)
    coefficient = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producttype'


class Sales(models.Model):
    saleid = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Products, models.DO_NOTHING, db_column='productid', blank=True, null=True)
    partnerid = models.ForeignKey(Partners, models.DO_NOTHING, db_column='partnerid', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    saledate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'
