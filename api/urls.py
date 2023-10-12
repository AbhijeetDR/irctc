from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', login_user, name = 'login'),
    path('trains/create', create_train, name="create_train"),
    path('trains/availability', availability, name='availability'),
    path('trains/<int:pk>/book', book, name="book_ticket"),
    path('bookings/<int:pk>', booking_detail, name='booking_detail'),
]