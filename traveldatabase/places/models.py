from django.db import models

# Create your models here.
from django.db import models

class Places(models.Model):
    column1 = models.IntegerField(db_column='Column1')
    state = models.CharField(db_column='State',max_length=100, blank=True, null=True)
    city = models.CharField(db_column='City',max_length=100, blank=True, null=True)
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)
    name = models.CharField(db_column='Name',max_length=255, blank=True, null=True)
    city = models.CharField(db_column='City',max_length=100, blank=True, null=True)
    google_review_rating = models.DecimalField(db_column='Google Review Rating',max_digits=3, decimal_places=1)
    entry_fee_in_inr = models.DecimalField(db_column='Entrance Fee in INR',max_digits=6, decimal_places=2, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'places'

