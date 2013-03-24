from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    founder = models.CharField(max_length=30, blank=True)
    number_of_employees = models.IntegerField(blank=True)
    date_founded = models.DateField(blank=True)
    
    def __unicode__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer)
    mileage = models.IntegerField(blank=True)
    fabrication_date = models.DateField(blank=True)
    price = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m', blank=True)
    
    def __unicode__(self):
        return self.manufacturer.name + " " + self.name