from django.db import models

class Train(models.Model):
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    seat_capacity = models.PositiveIntegerField()
    arrival_time_at_source = models.TimeField()
    arrival_time_at_destination = models.TimeField()
    available = models.IntegerField(null = True, blank = True)
    start_seat = models.IntegerField(null=True, blank = True, default = 1)

class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    no_of_seats = models.PositiveIntegerField()
    starting_seat = models.IntegerField()

