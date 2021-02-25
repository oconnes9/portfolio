from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models

def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    items = models.Item.objects.all()
    listDirectories = [[item.fileName, item.pictureName, item.price] for item in items]
    contextDict = {
        "listDirectories": listDirectories
    }

    return render(request,'portfolio.html',context=contextDict)

def portfolioAddButton(request):
    itemDict = {
        "fileUpload": request.FILES['fileUpload'],
        "fileName": request.POST['fileName'],
        "pictureName": request.POST['pictureName'],
        "price": float(request.POST['price'])
    }
    newItem = models.Item(**itemDict)
    newItem.handle_file()
    newItem.save()

    return JsonResponse({"Message":"Success"})

def portfolioAdd(request):
    return render(request,'addItem.html')

def submitContactForm(request):
    formDict = {
        "name": request.POST['fullName'],
        "email": request.POST['emailAddress'],
        "message": request.POST['message']
    }
    newEmail = models.Email(**formDict)
    #Send comment, name and email to MY email and send response to persons email to say we have received query.
    #Return "Query submitted" page
    return JsonResponse(formDict)