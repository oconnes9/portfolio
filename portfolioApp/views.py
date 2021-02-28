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
    contextDict = models.Item.getAllItems()
    return render(request,'portfolio.html',context=contextDict)

def portfolioAddButton(request):
    itemDict = {
        "fileUpload": request.FILES['fileUpload'],
        "fileName": request.POST['fileName'],
        "pictureName": request.POST['pictureName'],
        "price": float(request.POST['price'])
    }
    try:
        newItem = models.Item(**itemDict)
        newItem.handle_file()
        newItem.save()
        return render(request,'addItemSuccess.html')
    except:
        return render(request, 'addItemFailure.html')

def portfolioAdd(request):
    return render(request,'addItem.html')

def portfolioUpdate(request):
    contextDict = models.Item.getAllItems()
    return render(request,'updateItem.html',context=contextDict)

def portfolioUpdateButton(request):


    try:
        item = models.Item.objects.get(fileName=request.POST['selectItem'])
        item.pictureName = request.POST['pictureName']
        item.price = float(request.POST['price'])
        item.save()
        return render(request, 'updateItemSuccess.html')
    except:
        return render(request, 'updateItemFailure.html')

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