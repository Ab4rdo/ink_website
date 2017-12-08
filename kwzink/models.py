from django.db import models

class Ink(models.Model):
    batch_number = models.CharField(max_length=6)
    name_EN = models.CharField(max_length=40)
    name_PL = models.CharField(max_length=40)
    INK_TYPE_CHOICE = (
        ('St', 'Standard'),
        ('IG', 'Iron-Gal'),
    )
    ink_type = models.CharField(
            max_length=8,
            choices = INK_TYPE_CHOICE,
    )

    def __str__(self):
        return '{} {}'.format(self.batch_number, self.name_EN)

