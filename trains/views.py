from django.shortcuts import render, redirect
from .forms import TrainCreationForm, AvailabilityForm, TicketBookForm
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
def create(request):
    if request.method == 'POST' and request.user.is_superuser ==True:
        form = TrainCreationForm(request.POST)
        if form.is_valid():
            train = form.save()
            return HttpResponse("Train ccreated successfully")

    form = TrainCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'trains/create_train.html', context)

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
            return HttpResponse("invalid input")

def book(request, pk):
    form = TicketBookForm()
    if request.method == "POST":
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

    return render(request, "trains/book.html", {'form' : form})