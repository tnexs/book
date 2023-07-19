from django.db import models
from django.urls import reverse
# Create your models here.

class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    authors = models.ForeignKey(Authors, related_name='book',on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

