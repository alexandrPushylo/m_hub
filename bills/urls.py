from django.urls import path
from bills.views import edit_electricity

urlpatterns = [
    path('edit_electricity/', edit_electricity, name='edit_electricity'),
]
