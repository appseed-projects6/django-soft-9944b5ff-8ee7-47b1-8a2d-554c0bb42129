# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    stack = models.CharField(max_length=255, null=True, blank=True)
    unit_of_measure = models.CharField(max_length=255, null=True, blank=True)
    last_updated = models.CharField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Serialnumber(models.Model):

    #__Serialnumber_FIELDS__
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    stock = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.CharField(max_length=255, null=True, blank=True)
    supplier_invoice = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)

    #__Serialnumber_FIELDS__END

    class Meta:
        verbose_name        = _("Serialnumber")
        verbose_name_plural = _("Serialnumber")


class Taxrate(models.Model):

    #__Taxrate_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Taxrate_FIELDS__END

    class Meta:
        verbose_name        = _("Taxrate")
        verbose_name_plural = _("Taxrate")


class Invoice(models.Model):

    #__Invoice_FIELDS__
    customer = models.CharField(max_length=255, null=True, blank=True)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)

    #__Invoice_FIELDS__END

    class Meta:
        verbose_name        = _("Invoice")
        verbose_name_plural = _("Invoice")


class Invoiceline(models.Model):

    #__Invoiceline_FIELDS__
    invoice = models.CharField(max_length=255, null=True, blank=True)
    stock = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    serial_numbers = models.CharField(max_length=255, null=True, blank=True)

    #__Invoiceline_FIELDS__END

    class Meta:
        verbose_name        = _("Invoiceline")
        verbose_name_plural = _("Invoiceline")


class Sale(models.Model):

    #__Sale_FIELDS__
    stock = models.CharField(max_length=255, null=True, blank=True)
    invoice = models.CharField(max_length=255, null=True, blank=True)
    supplier_details = models.CharField(max_length=255, null=True, blank=True)

    #__Sale_FIELDS__END

    class Meta:
        verbose_name        = _("Sale")
        verbose_name_plural = _("Sale")


class Quote(models.Model):

    #__Quote_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    quote_number = models.CharField(max_length=255, null=True, blank=True)
    quote_line = models.CharField(max_length=255, null=True, blank=True)

    #__Quote_FIELDS__END

    class Meta:
        verbose_name        = _("Quote")
        verbose_name_plural = _("Quote")


class Quoteline(models.Model):

    #__Quoteline_FIELDS__
    quote = models.CharField(max_length=255, null=True, blank=True)
    stock = models.CharField(max_length=255, null=True, blank=True)

    #__Quoteline_FIELDS__END

    class Meta:
        verbose_name        = _("Quoteline")
        verbose_name_plural = _("Quoteline")


class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    erf = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Lead(models.Model):

    #__Lead_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    phase = models.CharField(max_length=255, null=True, blank=True)
    representative = models.CharField(max_length=255, null=True, blank=True)

    #__Lead_FIELDS__END

    class Meta:
        verbose_name        = _("Lead")
        verbose_name_plural = _("Lead")


class Supplier(models.Model):

    #__Supplier_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__Supplier_FIELDS__END

    class Meta:
        verbose_name        = _("Supplier")
        verbose_name_plural = _("Supplier")



#__MODELS__END
