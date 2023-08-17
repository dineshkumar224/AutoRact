from django.urls import path
from . import views

urlpatterns = [
    #path('', views.upload, name='upload'),
    #path('', views.autoract, name='autoract'),
    path('kyc', views.autoract, name='autoract'),
    path('upload-image', views.uploadImage, name='uploadImage'),
    path('store-data', views.storeData, name='storeData')

]
