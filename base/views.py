from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from trains.models import Booking
from django.http import JsonResponse
# Create your views here.

def signup(request):
    form = SignupForm()
    context = {
        'form' : form
    }
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    return render(request, 'base/signup.html', context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                context = {'msg': "Logged in successfully"}
                return render(request, 'base/msg.html', context)
            else:
                context = {'msg': "Invalid credentials"}
                return render(request, 'base/msg.html', context)
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'base/login.html', context)


def booking(request, pk):
    booking = Booking.objects.get(id = pk)
    data = {
        'booking_id' : booking.id,
        'train_id' : booking.train.id,
        'train_name' : booking.train.train_name,
        'user_id' : booking.user.id,
        'no_of_seats' : booking.no_of_seats,
        'seat_no' : [i for i in range(booking.starting_seat, booking.starting_seat + booking.no_of_seats)],
        'arrival_time' : booking.train.arrival_time_at_source,
        'destination_time' : booking.train.arrival_time_at_destination,
    }
    return JsonResponse(data)
