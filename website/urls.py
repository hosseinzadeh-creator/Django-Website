from django.urls import path
from . import views 
#from website.views import *

urlpatterns = [
    path('',views.index_view),
    path('aboutus',views.aboutus_view),
    pat('contactus',views.contactus_view)
]
