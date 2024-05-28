from django.shortcuts import render

# Create your views here.


def dashboard(request):
    out = {}
    return render(request, 'dashboard/dashboard.html', out)
