from django.db import models

class Email(models.Model):

    name = models.CharField(max_length=60)
    email = models.CharField(max_length=80)
    message = models.CharField(max_length=500)

    @classmethod
    def create(cls, name, email, message):
        return cls(name=name, email=email, message=message)


    #Write method to send email


class Item(models.Model):

    fileName = models.CharField(max_length=60, unique=True)
    pictureName = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def create(cls, fileName, pictureName, price):
        return cls(fileName=fileName, pictureName=pictureName, price=price)

    #Need method to find existing items and to add to database