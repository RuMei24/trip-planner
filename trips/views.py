from django.shortcuts import render, redirect, get_object_or_404
from .forms import TripForm, PreferenceForm
from .models import Trip, Preference

def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save()
            return redirect('trip_detail', trip_code=trip.trip_code)
    else:
        form = TripForm()

    return render(request, 'trips/create_trip.html', {'form': form})


def trip_detail(request, trip_code):
    trip = get_object_or_404(Trip, trip_code=trip_code)
    return render(request, 'trips/trip_detail.html', {'trip': trip})

def submit_preference(request, trip_code):
    trip = get_object_or_404(Trip, trip_code=trip_code)

    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            Preference = form.save(commit=False)
            Preference.trip = trip
            Preference.save()
            return redirect('trip_detail', trip_code=trip.trip_code)
    else:
            form = PreferenceForm()

    return render(request, 'trips/submit_preference.html', {'form': form, 'trip': trip})

def generate_itinerary(request, trip_code):
    trip = get_object_or_404(Trip, trip_code=trip_code)
    preferences = Preference.objects.filter(trip=trip)

    itinerary = "Day 1: Visit popular attractions and blah"

    return render(request, 'trips/generate_itinerary.html',{
        'trip': trip,
        'itenarary': itinerary,
    })


