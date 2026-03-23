from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length= 255, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    price = models.IntegerField()
    created = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.title
