from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    description_auto = models.TextField()

    def __str__(self):
        return self.model


class Details(models.Model):
    model_details = models.CharField(max_length=40)
    vin = models.IntegerField()
    description_details = models.TextField()

    def __str__(self):
        return self.model_details
