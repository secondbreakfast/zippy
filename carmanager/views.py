from django.shortcuts import render, redirect
from carmanager.models import Car
from carmanager.forms import CarForm
import csv

#On homepage load, imports CSV into database. This happens every time, so there are lots of duplicate records.
def import_cars(request):
    url = 'carmanager/static/cars.csv'
    with open(url, "rU") as f:
        reader = csv.reader(f)
        for row in reader:
            Car.objects.create(year=row[0], make=row[1], model=row[2], horsepower=row[3], transmission=row[4], gears=row[5])
    return render(request, "home.html")

#Displays search form.
def search_form(request):
    return render(request, 'search_cars.html')

#Takes user search input and queries database, returning results to another page called "search_results". Checks for some errors.
#I wanted this to take in multiple search fields but couldn't get it to work properly-- all fields are optional.
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

#From search results, a user can  click on a record to edit. On success, redirects to homepage.
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

# User can also delete a record directly from the search list. On success, redirects to homepage.
def delete_cars(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect("/")

#Allows user to add a new car to the database.
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