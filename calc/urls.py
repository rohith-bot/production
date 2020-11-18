from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('rashmi',views.rashmi,name='rashmi'),
    path('sandesh',views.sandesh,name='sandesh'),
    path('submitras',views.submitras,name='submitras'),
    path('submitsan',views.submitsan,name='submitsan')
]
