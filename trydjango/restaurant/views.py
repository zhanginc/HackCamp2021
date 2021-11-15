from django.shortcuts import render

from .forms import RestaurantForm
from .models import Restuarant


# Create your views here.
def restaurant_create_view(request):
    def get(self, request):
        form = RestaurantForm()
        context = {'form' : form}
        return render(request, "restaurant_view.html", context)