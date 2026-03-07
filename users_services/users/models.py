from django.db import models


class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Empleado(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name