from django.urls import path   #imported this module
from . import views   #imported
#from website.views import *

urlpatterns = [
    path('',views.index_view),
    path('aboutus',views.aboutus_view),
    path('contactus',views.contactus_view)
]   #defined this urls path 
