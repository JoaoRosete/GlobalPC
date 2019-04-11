import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse


def get_image_path(instance, filename):
    return os.path.join('loja/static/images', str(instance.id), filename)


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category_subcategory', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default="product")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    featured = models.BooleanField(default=True)
    news = models.BooleanField(default=False)
    highlights = models.BooleanField(default=False)
    opportunity = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name='subcategory_products', on_delete=models.CASCADE, default='')
    brand = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='')
    postal_code = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):  # Associar o User utilizado no admin/user criado para associar a um User Profile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Purchase(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default='')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default='')

    def __str__(self):
       return  self.user.user.username + ' ' + self.product.title
