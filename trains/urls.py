from django.urls import path
from .views import *
urlpatterns = [
    path('create', create, name = "create"),
    path('availability/', availability, name="availability"),
    path('<int:pk>/book', book, name = "book_train")
]