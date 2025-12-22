from django.urls import path
from . import views

urlpatterns = [
               path('',views.index_view),
               path('chocolate/',views.choclate_view),
               path('baking_ingredients/',views.baking_view),
               path('decorating_supplies/',views.decorating_view),
               path('pastry_necessities/',views.pastry_view),
               path('chocolate/<int:chocolates>/',views.chocolateCat_number_view),# If integer data is entered in the page URL, then the user will be redirected to the corresponding page.
               path('chocolate/<str:chocolates>/',views.chocolateCat_view, name='chocolateCat_Name') #Specifying the path address name for dynamicization             
    ]
