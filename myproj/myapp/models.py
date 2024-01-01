from django.db import models

# Create your models here.
class BookModel(models.Model):
    bname = models.CharField(max_length=30)
    bprice = models.IntegerField()
    bauthor = models.CharField(max_length=30)

    def __str__(self):
        return self.bname
    
class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name