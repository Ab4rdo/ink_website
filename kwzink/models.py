from django.db import models

class Ink(models.Model):
    batch_number = models.CharField(max_length=6)
    name_EN = models.CharField(max_length=40)
    name_PL = models.CharField(max_length=40)
    TYPE_CHOICE = (
        'Standard',
        'IG',
        'Pigment',
        'Other',
    ) 

    def __str__(self):
        return name_EN

