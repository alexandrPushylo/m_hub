from django.urls import path
from debt_manager.views import edit_debt_view, personal_debt_view

urlpatterns = [
    path('edit_debt/', edit_debt_view, name='edit_debt'),
    path('personal_debt/', personal_debt_view, name='personal_debt')
]
