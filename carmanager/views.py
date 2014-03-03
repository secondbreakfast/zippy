from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.template import RequestContext
from carmanager.models import Car
from carmanager.forms import CarForm
import csv


def import_cars(request):
    url = 'carmanager/static/cars.csv'
    with open(url, "rU") as f:
        reader = csv.reader(f)
        for row in reader:
            Car.objects.create(year=row[0], make=row[1], model=row[2], horsepower=row[3], transmission=row[4], gears=row[5])
    return render(request, "home.html")

def search_form(request):
    return render(request, 'search_cars.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            cars = Car.objects.filter(make__icontains=q)
            return render(request, 'search_results.html',
                {'cars': cars, 'query': q})
    return render(request, 'search_cars.html',
        {'error': error})

def edit_cars(request,car_id):
    edit_car = Car.objects.get(id=car_id)
    if request.method=="POST":
        form = CarForm(request.POST, instance=edit_car)
        if form.is_valid():
            if form.save():
                return redirect("/")
                # return redirect("/cars/{}".format(car_id))
    else:
        form = CarForm(instance=edit_car)

    data = {"car": edit_car, "form": form}
    return render (request, "edit_cars.html", data)

def delete_cars(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect("/")


def add_cars(request):
    if request.method=="POST":
        form = CarForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/")
    else:
        form = CarForm()
    data = {'form': form}
    return render(request, "add_cars.html", data)