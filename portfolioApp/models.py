from django.db import models
import os
from pathlib import Path

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
    fileUpload = models.FileField(null=True)

    @classmethod
    def create(cls, fileUpload, fileName, pictureName, price):
        return cls(fileUpload=fileUpload, fileName=fileName, pictureName=pictureName, price=price)

    def handle_file(self):

        BASE_DIR = Path(__file__).resolve().parent.parent
        STATIC_DIR = os.path.join(BASE_DIR, 'static')
        finalDir = os.path.join(STATIC_DIR, self.fileName)
        with open(finalDir, 'wb+') as destination:
            for chunk in self.fileUpload.chunks():
                destination.write(chunk)

    @classmethod
    def getAllItems(cls):
        items = cls.objects.all()
        listDirectories = [[item.fileName, item.pictureName, item.price] for item in items]
        contextDict = {
            "listDirectories": listDirectories
        }
        return contextDict


    #Need method to find existing items and to add to database