from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
      user = models.ForeignKey(User , on_delete=models.CASCADE)
      name = models.CharField(max_length=200)
      description = models.TextField()
      price = models.PositiveIntegerField(default=0)
      numbers = models.PositiveIntegerField(default=0)

      date_created = models.DateTimeField(auto_now=True)
      date_modified = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return f'{self.user} : {self.name}'