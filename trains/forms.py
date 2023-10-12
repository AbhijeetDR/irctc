from django import forms
from .models import Train
class TrainCreationForm(forms.ModelForm):
    class Meta:
        model = Train
        exclude = ()

class AvailabilityForm(forms.Form):
    source = forms.CharField()
    destination = forms.CharField()

class TicketBookForm(forms.Form):
    train_id = forms.IntegerField()
    no_of_seats = forms.IntegerField()

