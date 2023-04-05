from django.db import models

# Create your models here.

class PincodeData(models.Model):
    pincode = models.IntegerField()
    dictrict = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.pincode)

