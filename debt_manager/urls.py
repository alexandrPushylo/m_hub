from django.urls import path
from debt_manager.views import edit_debt_view

urlpatterns = [
    path('edit_debt/', edit_debt_view, name='edit_debt')
]
