import uuid

# core django
from django.db import models

# third party
from model_utils.models import TimeStampedModel


class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank_name = models.CharField(max_length=180)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    branch = models.CharField(max_length=256)
    ifsc = models.CharField(max_length=15)
    bank_id = models.IntegerField()
    
    def __str__(self):
        return self.bank_name