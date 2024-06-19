from django.urls import path
from bills.views import edit_electricity, edit_cold_water, edit_hot_water, edit_rent

urlpatterns = [
    path('edit_electricity/', edit_electricity, name='edit_electricity'),
    path('edit_cold_water/', edit_cold_water, name='edit_cold_water'),
    path('edit_hot_water/', edit_hot_water, name='edit_hot_water'),
    path('edit_rent/', edit_rent, name='edit_rent'),
]
