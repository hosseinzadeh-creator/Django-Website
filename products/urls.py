from django.urls import path
from . import views

urlpatterns = [
               path('',views.index_view),
               path('chocolate',views.choclate_view),
               path('baking_ingredients',views.baking_view),
               path('decorating_supplies',views.decorating_view),
               path('pastry_necessities',views.pastry_view)
                              
    ]
