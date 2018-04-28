from django.db import models


class Admin(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255)


class Abonent(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255)


class Person(models.Model):
    abonent_id = models.IntegerField()
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)