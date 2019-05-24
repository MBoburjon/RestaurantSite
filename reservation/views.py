from django.shortcuts import render
from .forms import ReserveTableForm
# Create your views here.

from reservation.models import Reservation

def reserve_table(request):

    context = {}

    return render(request, 'reservation/reservation.html', context)