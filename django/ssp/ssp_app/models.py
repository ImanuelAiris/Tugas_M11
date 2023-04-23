from django.db import models

class Sistem1(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sistem2(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Sistem3(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
