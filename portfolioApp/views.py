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

def portfolioItem(request, name):
    item = models.Item.objects.get(fileName=name)
    contextDict = item.__dict__
    return render(request, 'item.html',context=contextDict)

def portfolioAdd(request):
    return render(request,'addItem.html')

def portfolioDelete(request):
    contextDict = models.Item.getAllItems()
    return render(request,'deleteItem.html',context=contextDict)

def portfolioUpdate(request):
    contextDict = models.Item.getAllItems()
    return render(request,'updateItem.html',context=contextDict)

def portfolioAddButton(request):
    itemDict = {
        "fileUpload": request.FILES['fileUpload'],
        "fileName": request.POST['fileName'],
        "pictureName": request.POST['pictureName'],
        "price": float(request.POST['price'])
    }
    contextDict = {
        "action": "portfolioAdd"
    }
    try:
        newItem = models.Item(**itemDict)
        newItem.handle_file()
        newItem.save()
        contextDict["message"] = "Item Added!"
        return render(request,'itemUpdateMessage.html',context=contextDict)
    except:
        contextDict["message"] = "Could not add item"
        return render(request, 'itemUpdateMessage.html',context=contextDict)


def portfolioUpdateButton(request):
    contextDict = {
        "action": "portfolioUpdate"
    }
    try:
        item = models.Item.objects.get(fileName=request.POST['selectItem'])
        item.pictureName = request.POST['pictureName']
        item.price = float(request.POST['price'])
        item.save()
        contextDict["message"] = "Item Updated!"
        return render(request, 'itemUpdateMessage.html', context=contextDict)
    except:
        contextDict["message"] = "Could not update item"
        return render(request, 'itemUpdateMessage.html', context=contextDict)

def portfolioDeleteButton(request):
    contextDict = {
        "action": "portfolioDelete"
    }
    try:
        item = models.Item.objects.get(fileName=request.POST['selectItem'])
        item.delete()
        contextDict["message"] = "Item Deleted!"
        return render(request, 'itemUpdateMessage.html', context=contextDict)
    except:
        contextDict["message"] = "Could not delete item"
        return render(request, 'itemUpdateMessage.html', context=contextDict)


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