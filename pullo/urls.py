from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('contact.html',views.contact,name='contact'),
    path('about.html',views.about,name='about'),
    path('index.html',views.home,name='home'),
    path('brand.html',views.brand,name="brand"),
    path('detail/<int:pk>', views.detail,name='detail'),
    path('detail/detail/index.html',views.home,name='home'),
    path('detail/detail/brand.html',views.redirectToBrand,name='redirectToBrand'),
    path('detail/detail/contact.html',views.contact , name='contact'),
    path('commanddetail/command.html',views.command,name='command'),
    path('commanddetail/index.html',views.home,name='home')
    
]