from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect




# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == "POST":
        print(request.PRINT)

    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def restaurant_view(request):
    return render(request, "restaurant_view.html")

# Generate restaurant prediction here


## The result page view 