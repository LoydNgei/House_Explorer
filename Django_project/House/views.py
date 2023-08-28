# House.views

from django.http import Http404
from django.shortcuts import render
from .models import houses
from .forms import HouseSearchForm

def home(request):
    is_featured = houses.objects.filter(is_featured=True)[:3]
    return render(request, 'House/home.html', {'title': 'Home', 'houses': is_featured})

def about(request):
    return render(request, 'House/about.html', {'title': 'About'})

def house_view(request):
    # Retrieve all house objects from the database
    all_houses = houses.objects.all()

    # Pass the data to the template
    return render(request, 'House/houses.html', {'title': 'Houses', 'houses': all_houses})

def search_houses(request):
    # Search the houses functionality
    form = HouseSearchForm(request.GET)
    all_houses = houses.objects.all()

    if form.is_valid():
        Search_house = form.cleaned_data.get('Search_house')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if Search_house:
            all_houses = all_houses.filter(name__icontains=Search_house)

        if min_price is not None:
            all_houses = all_houses.filter(price__gte=min_price)

        if max_price is not None:
            all_houses = all_houses.filter(price__lte=max_price)

    context = {
        'form': form,
        'houses': all_houses,
    }

    return render(request, 'House/houses.html', context)