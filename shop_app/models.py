from tabnanny import verbose
from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Name of clothes')
    def __str__(self):
        return self.title
class Gender_clothes(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Gender of clothes')
    def __str__(self):
        return self.title


class Clothes(models.Model):
    clothes_name = models.CharField(max_length = 50, verbose_name = 'Name of clothes')
    description = models.TextField(verbose_name = 'Description', max_length = 200)
    image = models.ImageField(null = True, verbose_name = 'Image')
    price = models.IntegerField(null = True, verbose_name = 'Prace')
    size = models.IntegerField( verbose_name = 'Size of clothes')
    color = models.CharField(max_length = 70,verbose_name = 'Color of clothes')
    brand_of_clothes = models.ForeignKey( Brand, on_delete = models.PROTECT, verbose_name = 'Brand of clothes')
    gender_of_clothes = models.ForeignKey( Gender_clothes, on_delete = models.PROTECT, verbose_name = 'Gender of clothes')
    publication = models.BooleanField(verbose_name = 'Publication', default = True)
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Update Time')


class Order(models.Model):
    full_name = models.CharField(max_length=100 ,verbose_name=' full_name')
    email = models.CharField(max_length=1000, verbose_name='email')
    password = models.CharField(max_length=50,verbose_name='password')
    address = models.CharField(max_length=1000, verbose_name='address')
    phone_number = models.CharField(max_length=50,verbose_name='phone_number',)
    name_products= models.TextField(verbose_name='name_products',)
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')

