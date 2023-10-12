from django.shortcuts import render
from base.forms import SignupForm

from trains.forms import *
from trains.models import *

from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        response_data = {
            'status' : "Account successfully created",
            'status_code' : 200,
            'user_id': user.id
        }
        return JsonResponse({'Response_Data': response_data})

def login_user(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        uname = form.cleaned_data['username']
        pwd = form.cleaned_data['password']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            response_data = {
                'status' : 'Login successful',
                'status_code' : 200,
                'user_id' : user.id,
            }

            return JsonResponse({'Response Data' : response_data})
        else:
            response_data = {
                'status' : "Incorrect username/password provided.Please retry",
                'status_code' : 401,
            }
            return  JsonResponse({'Response Data' : response_data})

def create_train(request):
    if request.method == 'POST' and request.user.is_superuser ==True:
        form = TrainCreationForm(request.POST)
        if form.is_valid():
            train = form.save()
            response_data = {
                "message" : "Train created successfully",
                'train_id' : train.id,
            }
            return JsonResponse({'Response Data' : response_data})


def availability(request):
    src = request.GET.get('source')
    des = request.GET.get('destination')
    if src and des:
        try:
            train = Train.objects.filter(source = src, destination = des)
            avail_trains = []
            for eachtrain in train:
                avail_trains.append({
                    'train_id' : eachtrain.id,
                    'train_name': eachtrain.train_name,
                    'available': eachtrain.available
                })
            return JsonResponse(avail_trains, safe = False)
        except:
            response_data = {
                'status_code' : 401,
                'message' : 'No train from source to destination',
            }
            return JsonResponse({'Response_Data' : response_data})

def book(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = TicketBookForm(request.POST)
        if form.is_valid():
            train_id = request.POST.get('train_id')
            no_of_seats = int(request.POST.get('no_of_seats'))
            train = Train.objects.get(id = train_id)
            booking = Booking(user = request.user,train = train, no_of_seats = no_of_seats, starting_seat = train.start_seat)
            booking.save()

            seat_no = [i for i in range(train.start_seat, train.start_seat + no_of_seats)]
            train.start_seat += no_of_seats
            train.save()
            return JsonResponse({'message' : 'Seat booked successfully ', 'booking_id' : booking.id, "seat_no" : seat_no})

def booking_detail(request, pk):
    booking = Booking.objects.get(id = pk)
    if booking.user == request.user:
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

