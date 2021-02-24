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
    listNames = [item.pictureName for item in items]
    listPrices = [item.price for item in items]
    contextDict = {
        "listDirectories": listDirectories
        #"listNames": listNames,
        #"listPrices": listPrices,
        #"numEntries": len(items)
    }


    NOTcontextDict = {}
    #for item in items:
     #   newDict = {"fileName": item.fileName, "pictureName": item.pictureName, "price": item.price}
      #  contextDict[item.fileName] = newDict

    print(contextDict)


    contextList = [item for item in items]


    return render(request,'portfolio.html',context=contextDict)

def portfolioAddButton(request):
    itemDict = {
        "fileName": request.POST['fileName'],
        "pictureName": request.POST['pictureName'],
        "price": float(request.POST['price'])
    }
    newItem = models.Item(**itemDict)
    newItem.save()

    return JsonResponse(itemDict)

def portfolioAdd(request):
    return render(request,'addItem.html')

#def findByFile(request, fileName):
  #  items = models.Item.objects.get(fileName=fileName)

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