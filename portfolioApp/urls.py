from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('portfolio',views.portfolio,name="portfolio"),
    path('portfolio/item/<str:name>',views.portfolioItem,name="portfolioItem"),
    path('portfolioAddButton',views.portfolioAddButton,name="portfolioAddButton"),
    path('submitcontactform',views.submitContactForm,name='submitcontactform'),
    path('portfolio/add',views.portfolioAdd,name="portfolioAdd"),
    path('portfolioUpdateButton',views.portfolioUpdateButton,name="portfolioUpdateButton"),
    path('portfolio/update',views.portfolioUpdate,name="portfolioUpdate"),
    path('portfolioDeleteButton',views.portfolioDeleteButton,name="portfolioDeleteButton"),
    path('portfolio/delete',views.portfolioDelete,name="portfolioDelete"),
    #path('portfolio/find/<str:fileName>',views.findByFile,name='findByFile')
]