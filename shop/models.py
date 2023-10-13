from django.db import models
from django.db.models.fields.related import ForeignKey


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return str(self.title)


class Command(models.Model):
    items = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=300, default=False)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    command_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['command_date']

    def __str__(self):
        return str(self.name)