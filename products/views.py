from django.shortcuts import render #Use the render command to display Html pages
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect #added HttpResponeRedirect 
from django.urls import reverse #imported for use name of url path
#from django.template.loader import render_to_string #imported for use template file


# Create your views here.

chocolateDict={
    'white-chocolate':'Since 1921, Merckens has been a trusted name for premium chocolate retail confectioners around the country and is a favorite in many circles. Merckens Bulk Superior White Wafers are a premium compound coating wafer beloved by confectioners everywhere for their superior flavor, smooth consistency, and ease of use. They’re great on their own as a snack, but can be easily worked into a recipe for enrobing, molding, & dipping, along with other uses.',
    'milk-chocolate':'Our decadent Milk Deluxe European Compound Coating features a creamy, balanced cocoa flavor with a smooth, velvety finish. It melts quickly into a thin, silky texture with the ease & workability of the finest European chocolates with no tempering required. Eleven o’one Deluxe compounds set with a thin, clean coating that won’t weigh down your treats or hide your details.',
    'dark-chocolate':'Our decadent Dark Deluxe European Compound Coating features a smooth, balanced flavor with rich cocoa notes. It melts quickly into a thin, silky texture with the ease & workability of the finest European chocolates with no tempering required. Eleven o’one Deluxe compounds set with a thin, clean coating that won’t weigh down your treats or hide your details. The deep cocoa flavor pairs beautifully with flavors like orange, espresso, toasted nuts or spiced chili.',
    'colored-white':'Colored Melting Wafers take your desserts to new heights with less effort! Specifically formulated to melt quickly into a smooth, velvet consistency for all of your chocolate-coated treats, our Sweet Shoppe Colored Melting wafers provide a full, even coating with exceptional shine & snap. Not only are they vibrant, our coating wafers are also easy to use - just melt - no tempering required!',
    'flavored-chocolate-wafers':'Our Sweet Shoppe Cream Cheese Melting Wafers add a rich & creamy cream cheese flavor to your treats! Designed to capture the taste of real cream cheese frosting, these wafers provide a rich, creamy flavor & soft finish. Please note these wafers are softer to the touch when compared to our standard formula & may take a bit longer to set, giving you time to perfect your dips, drizzles & molds.',
}

def index_view(request):
    return render(request,"products/index.html") #Use the render command to display Html pages 
    # renderData=render_to_string("products/index.html") #address of html file
    # return HttpResponse(renderData)
    #return HttpResponse('<h1>main producat page</h1>')

def choclate_view(request):

    chocolateProducts=list(chocolateDict.keys())
    context={
             'chocolateList':chocolateProducts
    }
    return render(request,'products/chocolate.html',context) #using the DTL method
    # chocolateItems=""
    # for item in chocolateProducts:
    #   chocolate_urlPath=reverse('chocolateCat_Name', args=[item]) #should be use the name of chocolateCat_view
    #   chocolateItems+=f'<li><a href="{chocolate_urlPath}"> {item} </a></li>\n'
    # content=f'<ul> {chocolateItems} </ul>'
   #This pattern is used for a limited number of items.
    # content="""
    #         <ul>
    #           <li><a href="#">white-chocolate</a></li>
    #           <li><a href="#">milk-chocolate</a></li>
    #           <li><a href="#">dark-chocolate</a></li>
    #           <li><a href="#">colored-white</a></li>
    #           <li><a href="#">flavored-chocolate-wafers</a></li>
    #        </ul>  
    # """
    # return HttpResponse(content)

def baking_view(request):
    return HttpResponse('<h1>baking ingredients page</h1>')

def decorating_view(request):
    return HttpResponse('<h1>decorating supplies page</h1>')

def pastry_view(request):
    return HttpResponse('<h1>pastry necessities page</h1>')

#sub category page for chocolate product
# created redirect data
def chocolateCat_number_view(request,chocolates):
    chocolateCatList=list(chocolateDict.keys())
    if chocolates>len(chocolateCatList):
        return HttpResponseNotFound('<h1>Error 404: page is not found </h1>')
    redirectData=chocolateCatList[chocolates-1]
    urlPath=reverse('chocolateCat_Name', args=[redirectData]) #dynamic path
    return HttpResponseRedirect(urlPath)
    #return HttpResponseRedirect(f'/products/chocolate/{redirectData}')

def chocolateCat_view(request,chocolates):
    chocolateData=chocolateDict.get(chocolates)
    if chocolateData is not None:
        context={
            'chocolateName':chocolates,
            'chocolateDesc':chocolateData
        }#use DTL(Django Template Language) 
        return render(request,'products/chocolatecat.html',context) #Using the render command to display pages with the DTL method 
        #return HttpResponse(f'<h1> {chocolates}</h1>\n <p>{chocolateData}</p>')
    return HttpResponseNotFound('<h1>Error 404: page is not found </h1>')