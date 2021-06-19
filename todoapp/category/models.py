from django.db import models
# Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=100, null=True)

   class Meta:
      verbose_name = ("Category")
      verbose_name_plural = ("Categories")

   def __str__(self):
      return self.name 