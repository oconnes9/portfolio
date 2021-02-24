from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('portfolio',views.portfolio,name="portfolio"),
    path('portfolioAddButton',views.portfolioAddButton,name="portfolioAddButton"),
    path('submitcontactform',views.submitContactForm,name='submitcontactform'),
    path('portfolio/add',views.portfolioAdd,name="portfolioAdd"),
    #path('portfolio/find/<str:fileName>',views.findByFile,name='findByFile')
]